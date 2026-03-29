// 初始化配置
var supabaseUrl = 'https://iwpnajbmceobbkvwqtmy.supabase.co';
var supabaseKey = 'sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT';
console.log('Supabase配置:', { supabaseUrl, supabaseKey });

// 使用REST API代替Supabase客户端库
var supabase = {
    from: function(table) {
        return {
            select: function(fields) {
                return {
                    eq: function(column, value) {
                        return {
                            order: function(column, options) {
                                return {
                                    then: function(callback) {
                                        // 构建REST API请求
                                        var url = `${supabaseUrl}/rest/v1/${table}?${column}=eq.${value}&order=${options.ascending ? '' : 'desc'}.${column}&select=${fields}`;
                                        console.log('请求URL:', url);
                                        
                                        return fetch(url, {
                                            method: 'GET',
                                            headers: {
                                                'apikey': supabaseKey,
                                                'Authorization': `Bearer ${supabaseKey}`,
                                                'Content-Type': 'application/json'
                                            }
                                        })
                                        .then(response => {
                                            if (!response.ok) {
                                                throw new Error(`HTTP error! status: ${response.status}`);
                                            }
                                            return response.json();
                                        })
                                        .then(data => {
                                            return callback({ data: data, error: null });
                                        })
                                        .catch(error => {
                                            console.error('请求失败:', error);
                                            return callback({ data: null, error: error });
                                        });
                                    }
                                };
                            }
                        };
                    }
                };
            },
            insert: function(data) {
                // 构建REST API请求
                var url = `${supabaseUrl}/rest/v1/${table}`;
                console.log('插入数据URL:', url);
                console.log('插入数据:', data);
                
                return fetch(url, {
                    method: 'POST',
                    headers: {
                        'apikey': supabaseKey,
                        'Authorization': `Bearer ${supabaseKey}`,
                        'Content-Type': 'application/json',
                        'Prefer': 'return=representation'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    return { data: data, error: null };
                })
                .catch(error => {
                    console.error('插入失败:', error);
                    return { data: null, error: error };
                });
            }
        };
    }
};

console.log('使用REST API初始化完成');

// 修复loadEvents和loadInteractions函数，使其与REST API实现兼容
async function loadEvents() {
    try {
        console.log('开始加载事件记录...');
        
        // 直接使用fetch API获取数据
        var url = `${supabaseUrl}/rest/v1/event_records?is_deleted=eq.false&order=record_date.desc&select=*`;
        console.log('请求URL:', url);
        
        // 使用Promise.race添加超时机制
        var timeoutPromise = new Promise(function(_, reject) {
            setTimeout(function() { reject(new Error('请求超时')); }, 10000);
        });
        
        var fetchPromise = fetch(url, {
            method: 'GET',
            headers: {
                'apikey': supabaseKey,
                'Authorization': `Bearer ${supabaseKey}`,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        });
        
        var data = await Promise.race([fetchPromise, timeoutPromise]);
        console.log('事件记录加载成功:', data);
        eventList.innerHTML = '';
        
        if (data.length === 0) {
            eventList.innerHTML = '<div class="empty">暂无记录</div>';
            return;
        }
        
        data.forEach(function(event) {
            var eventItem = document.createElement('div');
            eventItem.className = 'event-item';
            
            var eventTime = document.createElement('div');
            eventTime.className = 'event-time';
            eventTime.textContent = new Date(event.record_date).toLocaleString();
            
            var eventContent = document.createElement('div');
            eventContent.className = 'event-content';
            var content = event.event_type;
            if (event.other_content) {
                content += ' (' + event.other_content + ')';
            }
            eventContent.textContent = content;
            
            var eventRemark = document.createElement('div');
            eventRemark.className = 'event-remark';
            if (event.remark) {
                eventRemark.textContent = '备注: ' + event.remark;
            }
            
            eventItem.appendChild(eventTime);
            eventItem.appendChild(eventContent);
            if (event.remark) {
                eventItem.appendChild(eventRemark);
            }
            
            eventList.appendChild(eventItem);
        });
    } catch (error) {
        console.error('加载事件记录出错:', error);
        eventList.innerHTML = '<div class="error">加载失败: ' + error.message + '</div>';
    }
}

// 加载互动记录
async function loadInteractions() {
    try {
        console.log('开始加载互动记录...');
        
        // 直接使用fetch API获取数据
        var url = `${supabaseUrl}/rest/v1/visitor_interact?order=interact_time.desc&select=*`;
        console.log('请求URL:', url);
        
        // 使用Promise.race添加超时机制
        var timeoutPromise = new Promise(function(_, reject) {
            setTimeout(function() { reject(new Error('请求超时')); }, 10000);
        });
        
        var fetchPromise = fetch(url, {
            method: 'GET',
            headers: {
                'apikey': supabaseKey,
                'Authorization': `Bearer ${supabaseKey}`,
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        });
        
        var data = await Promise.race([fetchPromise, timeoutPromise]);
        console.log('互动记录加载成功:', data);
        interactionList.innerHTML = '';
        
        if (data.length === 0) {
            interactionList.innerHTML = '<div class="empty">暂无互动记录</div>';
            return;
        }
        
        data.forEach(function(interaction) {
            var interactionItem = document.createElement('div');
            interactionItem.className = 'interaction-item';
            
            var interactionTime = document.createElement('div');
            interactionTime.className = 'interaction-time';
            interactionTime.textContent = new Date(interaction.interact_time).toLocaleString();
            
            var interactionContent = document.createElement('div');
            interactionContent.className = 'interaction-content';
            var content = interaction.visitor_name + ' - ' + interaction.interact_type;
            if (interaction.note) {
                content += ' (' + interaction.note + ')';
            }
            interactionContent.textContent = content;
            
            interactionItem.appendChild(interactionTime);
            interactionItem.appendChild(interactionContent);
            
            interactionList.appendChild(interactionItem);
        });
    } catch (error) {
        console.error('加载互动记录出错:', error);
        interactionList.innerHTML = '<div class="error">加载失败: ' + error.message + '</div>';
    }
}

// 提交互动
async function submitInteraction() {
    var visitorName = visitorNameInput.value.trim();
    
    if (!visitorName) {
        alert('请输入您的姓名');
        return;
    }
    
    if (!selectedInteractionType) {
        alert('请选择互动类型');
        return;
    }
    
    if (!supabase) {
        alert('Supabase客户端未初始化');
        return;
    }
    
    try {
        // 直接使用fetch API提交数据
        var url = `${supabaseUrl}/rest/v1/visitor_interact`;
        console.log('提交数据URL:', url);
        console.log('提交数据:', {
            visitor_name: visitorName,
            interact_type: selectedInteractionType
        });
        
        var response = await fetch(url, {
            method: 'POST',
            headers: {
                'apikey': supabaseKey,
                'Authorization': `Bearer ${supabaseKey}`,
                'Content-Type': 'application/json',
                'Prefer': 'return=representation'
            },
            body: JSON.stringify({
                visitor_name: visitorName,
                interact_type: selectedInteractionType
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        var data = await response.json();
        console.log('提交成功:', data);
        
        // 提交成功
        alert('提交成功');
        // 清空表单
        visitorNameInput.value = '';
        interactButtons.forEach(function(btn) { btn.classList.remove('active'); });
        selectedInteractionType = null;
        // 重新加载互动记录
        await loadInteractions();
    } catch (error) {
        console.error('提交互动出错:', error);
        alert('提交失败，请重试');
    }
}

// 全局变量
var selectedInteractionType = null;
var currentStatsRange = 'today';

// DOM元素
var eventList = document.getElementById('event-list');
var interactionList = document.getElementById('interaction-list');
var visitorNameInput = document.getElementById('visitor-name');
var submitButton = document.getElementById('submit-interaction');
var interactButtons = document.querySelectorAll('.interact-btn');
var eventTypeSelect = document.getElementById('event-type');
var otherContentRow = document.getElementById('other-content-row');
var otherContentInput = document.getElementById('other-content');
var remarkInput = document.getElementById('remark');
var saveEventButton = document.getElementById('save-event');
var statsButtons = document.querySelectorAll('.stats-btn');
var statsResult = document.getElementById('stats-result');

// 初始化
async function init() {
    console.log('开始初始化...');
    
    try {
        // 加载事件记录
        console.log('加载事件记录...');
        await loadEvents();
        console.log('事件记录加载完成');
        
        // 加载互动记录
        console.log('加载互动记录...');
        await loadInteractions();
        console.log('互动记录加载完成');
        
        // 加载统计
        console.log('加载统计...');
        await loadStats('today');
        console.log('统计加载完成');
        
        // 绑定事件
        console.log('绑定事件...');
        bindEvents();
        console.log('初始化完成');
    } catch (error) {
        console.error('初始化失败:', error);
        eventList.innerHTML = '<div class="error">初始化失败: ' + error.message + '</div>';
        interactionList.innerHTML = '<div class="error">初始化失败: ' + error.message + '</div>';
    }
}

// 绑定事件
function bindEvents() {
    // 事件类型选择变化
    eventTypeSelect.addEventListener('change', function() {
        if (this.value === '其他事项') {
            otherContentRow.style.display = 'flex';
        } else {
            otherContentRow.style.display = 'none';
            otherContentInput.value = '';
        }
    });
    
    // 保存事件按钮点击事件
    saveEventButton.addEventListener('click', async function() {
        await saveEvent();
    });
    
    // 统计按钮点击事件
    statsButtons.forEach(function(button) {
        button.addEventListener('click', async function() {
            // 移除所有按钮的active类
            statsButtons.forEach(function(btn) { btn.classList.remove('active'); });
            // 添加当前按钮的active类
            this.classList.add('active');
            // 加载对应时间范围的统计
            currentStatsRange = this.dataset.range;
            await loadStats(currentStatsRange);
        });
    });
    
    // 互动按钮点击事件
    interactButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // 移除所有按钮的active类
            interactButtons.forEach(function(btn) { btn.classList.remove('active'); });
            // 添加当前按钮的active类
            this.classList.add('active');
            // 记录选中的互动类型
            selectedInteractionType = this.dataset.type;
        });
    });
    
    // 提交互动按钮点击事件
    submitButton.addEventListener('click', async function() {
        await submitInteraction();
    });
    
    // 回车键提交
    visitorNameInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            submitInteraction();
        }
    });
}

// 保存事件
async function saveEvent() {
    var eventType = eventTypeSelect.value;
    var otherContent = eventType === '其他事项' ? otherContentInput.value.trim() : null;
    var remark = remarkInput.value.trim();
    
    if (eventType === '其他事项' && !otherContent) {
        alert('请输入具体事项');
        return;
    }
    
    try {
        var url = `${supabaseUrl}/rest/v1/event_records`;
        console.log('保存事件URL:', url);
        console.log('保存数据:', {
            event_type: eventType,
            other_content: otherContent,
            remark: remark
        });
        
        var response = await fetch(url, {
            method: 'POST',
            headers: {
                'apikey': supabaseKey,
                'Authorization': `Bearer ${supabaseKey}`,
                'Content-Type': 'application/json',
                'Prefer': 'return=representation'
            },
            body: JSON.stringify({
                event_type: eventType,
                other_content: otherContent,
                remark: remark,
                record_date: new Date().toISOString(),
                created_at: new Date().toISOString(),
                updated_at: new Date().toISOString(),
                is_deleted: false
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        var data = await response.json();
        console.log('保存成功:', data);
        
        alert('保存成功');
        // 清空表单
        eventTypeSelect.value = '吃饭';
        otherContentRow.style.display = 'none';
        otherContentInput.value = '';
        remarkInput.value = '';
        
        // 重新加载事件记录和统计
        await loadEvents();
        await loadStats(currentStatsRange);
    } catch (error) {
        console.error('保存事件出错:', error);
        alert('保存失败，请重试');
    }
}

// 加载统计
async function loadStats(timeRange) {
    try {
        console.log('开始加载统计:', timeRange);
        
        // 计算时间范围
        var now = new Date();
        var startDate, endDate;
        
        switch(timeRange) {
            case 'yesterday':
                var yesterday = new Date(now);
                yesterday.setDate(yesterday.getDate() - 1);
                startDate = new Date(yesterday.getFullYear(), yesterday.getMonth(), yesterday.getDate(), 0, 0, 0);
                endDate = new Date(yesterday.getFullYear(), yesterday.getMonth(), yesterday.getDate(), 23, 59, 59);
                break;
            case 'today':
                startDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
                endDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59);
                break;
            case 'this_week':
                var dayOfWeek = now.getDay();
                var diff = now.getDate() - dayOfWeek + (dayOfWeek === 0 ? -6 : 1);
                startDate = new Date(now.getFullYear(), now.getMonth(), diff, 0, 0, 0);
                endDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59);
                break;
            case 'this_month':
                startDate = new Date(now.getFullYear(), now.getMonth(), 1, 0, 0, 0);
                endDate = new Date(now.getFullYear(), now.getMonth() + 1, 0, 23, 59, 59);
                break;
            default:
                startDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
                endDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59);
        }
        
        var startStr = startDate.toISOString();
        var endStr = endDate.toISOString();
        
        // 构建URL
        var url = `${supabaseUrl}/rest/v1/event_records?is_deleted=eq.false&record_date=gte.${encodeURIComponent(startStr)}&record_date=lte.${encodeURIComponent(endStr)}&order=record_date.desc&select=*`;
        console.log('统计请求URL:', url);
        
        var response = await fetch(url, {
            method: 'GET',
            headers: {
                'apikey': supabaseKey,
                'Authorization': `Bearer ${supabaseKey}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        var data = await response.json();
        console.log('统计数据:', data);
        
        // 计算统计
        var stats = {};
        data.forEach(function(event) {
            var type = event.event_type;
            if (!stats[type]) {
                stats[type] = 0;
            }
            stats[type]++;
        });
        
        // 显示统计结果
        var rangeText = {
            'yesterday': '昨天',
            'today': '今天',
            'this_week': '本周',
            'this_month': '本月'
        };
        
        var html = `<div class="stats-title">${rangeText[timeRange]}统计</div>`;
        
        if (Object.keys(stats).length === 0) {
            html += '<div class="stat-item"><span>暂无记录</span></div>';
        } else {
            Object.keys(stats).forEach(function(type) {
                html += `<div class="stat-item"><span>${type}</span><span>${stats[type]}次</span></div>`;
            });
            html += `<div class="stat-item"><span>总计</span><span>${data.length}次</span></div>`;
        }
        
        statsResult.innerHTML = html;
    } catch (error) {
        console.error('加载统计出错:', error);
        statsResult.innerHTML = '<div class="error">加载统计失败: ' + error.message + '</div>';
    }
}



// 页面加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
