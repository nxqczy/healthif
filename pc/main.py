import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton, QListWidget, 
    QListWidgetItem, QMessageBox, QSplitter
)
from PyQt5.QtCore import Qt
from db import Database
from sync import SyncManager

class HealthRecordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        # Supabase配置
        self.supabase_url = "https://iwpnajbmceobbkvwqtmy.supabase.co"
        self.supabase_key = "sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT"
        self.sync_manager = SyncManager(self.supabase_url, self.supabase_key, self.db)
        
        self.init_ui()
        self.load_events()
        self.load_visitor_interactions()
    
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle('个人作息健康记录系统')
        self.setGeometry(100, 100, 800, 600)
        
        # 主布局
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        # 标题
        title_label = QLabel('PP的幸福记录')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        main_layout.addWidget(title_label)
        
        # 表单区域
        form_layout = QVBoxLayout()
        
        # 事件类型选择
        event_type_layout = QHBoxLayout()
        event_type_label = QLabel('事件类型:')
        self.event_type_combo = QComboBox()
        self.event_type_combo.addItems(['吃饭', '小便', '大便', '打针', '输液', '抽血', '检查', '其他事项'])
        self.event_type_combo.currentIndexChanged.connect(self.on_event_type_changed)
        event_type_layout.addWidget(event_type_label)
        event_type_layout.addWidget(self.event_type_combo)
        form_layout.addLayout(event_type_layout)
        
        # 其他事项输入框
        self.other_content_layout = QHBoxLayout()
        other_content_label = QLabel('其他事项:')
        self.other_content_edit = QLineEdit()
        self.other_content_edit.setEnabled(False)
        self.other_content_layout.addWidget(other_content_label)
        self.other_content_layout.addWidget(self.other_content_edit)
        form_layout.addLayout(self.other_content_layout)
        
        # 备注编辑框
        remark_layout = QHBoxLayout()
        remark_label = QLabel('备注:')
        self.remark_edit = QTextEdit()
        self.remark_edit.setFixedHeight(80)
        remark_layout.addWidget(remark_label)
        remark_layout.addWidget(self.remark_edit)
        form_layout.addLayout(remark_layout)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        self.save_button = QPushButton('保存')
        self.save_button.clicked.connect(self.save_event)
        self.delete_button = QPushButton('软删除')
        self.delete_button.clicked.connect(self.soft_delete_event)
        self.sync_button = QPushButton('同步到云端')
        self.sync_button.clicked.connect(self.sync_to_cloud)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.sync_button)
        form_layout.addLayout(button_layout)
        
        main_layout.addLayout(form_layout)
        
        # 分割器
        splitter = QSplitter(Qt.Vertical)
        
        # 记录列表和统计区域
        top_widget = QWidget()
        top_layout = QHBoxLayout(top_widget)
        
        # 记录列表
        self.event_list = QListWidget()
        self.event_list.itemClicked.connect(self.on_event_selected)
        top_layout.addWidget(self.event_list, 1)
        
        # 统计区域
        stats_widget = QWidget()
        stats_layout = QVBoxLayout(stats_widget)
        
        stats_label = QLabel('统计')
        stats_label.setAlignment(Qt.AlignCenter)
        stats_layout.addWidget(stats_label)
        
        # 快捷按钮
        quick_button_layout = QHBoxLayout()
        self.today_button = QPushButton('今天')
        self.today_button.clicked.connect(lambda: self.filter_events('today'))
        self.yesterday_button = QPushButton('昨天')
        self.yesterday_button.clicked.connect(lambda: self.filter_events('yesterday'))
        self.this_week_button = QPushButton('本周')
        self.this_week_button.clicked.connect(lambda: self.filter_events('this_week'))
        self.this_month_button = QPushButton('本月')
        self.this_month_button.clicked.connect(lambda: self.filter_events('this_month'))
        quick_button_layout.addWidget(self.today_button)
        quick_button_layout.addWidget(self.yesterday_button)
        quick_button_layout.addWidget(self.this_week_button)
        quick_button_layout.addWidget(self.this_month_button)
        stats_layout.addLayout(quick_button_layout)
        
        # 统计结果
        self.stats_result = QTextEdit()
        self.stats_result.setReadOnly(True)
        self.stats_result.setFixedHeight(100)
        stats_layout.addWidget(self.stats_result)
        
        top_layout.addWidget(stats_widget, 1)
        splitter.addWidget(top_widget)
        
        # 访客互动记录
        bottom_widget = QWidget()
        bottom_layout = QVBoxLayout(bottom_widget)
        
        visitor_label = QLabel('访客互动记录')
        visitor_label.setAlignment(Qt.AlignCenter)
        bottom_layout.addWidget(visitor_label)
        
        self.visitor_list = QListWidget()
        bottom_layout.addWidget(self.visitor_list)
        
        splitter.addWidget(bottom_widget)
        main_layout.addWidget(splitter)
    
    def on_event_type_changed(self):
        """事件类型变化时的处理"""
        if self.event_type_combo.currentText() == '其他事项':
            self.other_content_edit.setEnabled(True)
        else:
            self.other_content_edit.setEnabled(False)
            self.other_content_edit.clear()
    
    def save_event(self):
        """保存事件记录"""
        event_type = self.event_type_combo.currentText()
        other_content = self.other_content_edit.text() if event_type == '其他事项' else None
        remark = self.remark_edit.toPlainText()
        
        try:
            self.db.add_event(event_type, other_content, remark)
            QMessageBox.information(self, '成功', '事件记录保存成功')
            self.load_events()
            self.clear_form()
        except Exception as e:
            QMessageBox.error(self, '错误', f'保存失败: {str(e)}')
    
    def soft_delete_event(self):
        """软删除事件记录"""
        selected_item = self.event_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, '警告', '请选择要删除的事件')
            return
        
        event_id = selected_item.data(Qt.UserRole)
        try:
            success = self.db.soft_delete_event(event_id)
            if success:
                QMessageBox.information(self, '成功', '事件记录已软删除')
                self.load_events()
            else:
                QMessageBox.error(self, '错误', '删除失败')
        except Exception as e:
            QMessageBox.error(self, '错误', f'删除失败: {str(e)}')
    
    def sync_to_cloud(self):
        """同步到云端"""
        try:
            success, message = self.sync_manager.sync_to_cloud()
            if success:
                QMessageBox.information(self, '成功', message)
                self.load_visitor_interactions()
            else:
                QMessageBox.error(self, '错误', message)
        except Exception as e:
            QMessageBox.error(self, '错误', f'同步失败: {str(e)}')
    
    def load_events(self):
        """加载事件记录"""
        self.event_list.clear()
        events = self.db.get_all_events()
        
        for event in events:
            item_text = f"{event['record_date'][:19]} - {event['event_type']}"
            if event['other_content']:
                item_text += f" ({event['other_content']})"
            if event['remark']:
                item_text += f" - {event['remark']}"
            
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, event['id'])
            self.event_list.addItem(item)
    
    def load_visitor_interactions(self):
        """加载访客互动记录"""
        self.visitor_list.clear()
        interactions = self.db.get_visitor_interactions()
        
        for interaction in interactions:
            item_text = f"{interaction['interact_time'][:19]} - {interaction['visitor_name']} - {interaction['interact_type']}"
            if interaction.get('note'):
                item_text += f" ({interaction['note']})"
            
            item = QListWidgetItem(item_text)
            self.visitor_list.addItem(item)
    
    def on_event_selected(self, item):
        """选择事件时的处理"""
        # 可以在这里添加事件详情的显示逻辑
        pass
    
    def filter_events(self, time_range):
        """根据时间范围筛选事件"""
        self.event_list.clear()
        events = self.db.get_events_by_time_range(time_range)
        
        for event in events:
            item_text = f"{event['record_date'][:19]} - {event['event_type']}"
            if event['other_content']:
                item_text += f" ({event['other_content']})"
            if event['remark']:
                item_text += f" - {event['remark']}"
            
            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, event['id'])
            self.event_list.addItem(item)
        
        # 更新统计结果
        self.update_stats(time_range, events)
    
    def update_stats(self, time_range, events):
        """更新统计结果"""
        stats_text = f"{time_range}统计:\n"
        event_types = {}
        
        for event in events:
            event_type = event['event_type']
            if event_type not in event_types:
                event_types[event_type] = 0
            event_types[event_type] += 1
        
        for event_type, count in event_types.items():
            stats_text += f"{event_type}: {count}次\n"
        
        stats_text += f"总计: {len(events)}次"
        self.stats_result.setText(stats_text)
    
    def clear_form(self):
        """清空表单"""
        self.event_type_combo.setCurrentIndex(0)
        self.other_content_edit.clear()
        self.remark_edit.clear()

def test_sync():
    """测试同步功能"""
    from db import Database
    from sync import SyncManager
    
    # 初始化数据库
    db = Database()
    
    # Supabase配置
    supabase_url = "https://iwpnajbmceobbkvwqtmy.supabase.co"
    supabase_key = "sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT"
    
    # 初始化同步管理器
    sync_manager = SyncManager(supabase_url, supabase_key, db)
    
    # 测试添加事件
    print("测试添加事件...")
    db.add_event("吃饭", None, "测试记录")
    db.add_event("打针", None, "测试记录")
    db.add_event("输液", None, "测试记录")
    
    # 测试同步到云端
    print("\n测试同步到云端...")
    success, message = sync_manager.sync_to_cloud()
    print(f"同步结果: {success}, 消息: {message}")
    
    # 测试从云端获取数据
    print("\n测试从云端获取数据...")
    events = sync_manager.get_events_from_cloud()
    print(f"从云端获取到 {len(events)} 条事件记录")
    
    # 测试从云端获取互动记录
    print("\n测试从云端获取互动记录...")
    interactions = sync_manager.get_visitor_interactions_from_cloud()
    print(f"从云端获取到 {len(interactions)} 条互动记录")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HealthRecordApp()
    window.show()
    sys.exit(app.exec_())
