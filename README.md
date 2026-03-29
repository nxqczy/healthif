# 个人作息健康记录系统

## 项目简介
个人作息健康记录系统是一个PC端为主的健康记录应用，支持本地存储和云端同步，同时提供Web端静态页面供访客查看和互动。

### 主要功能
- PC端：事件记录、统计分析、云端同步
- Web端：查看记录、访客互动

## 技术栈
- PC端：Python + PyQt5 + SQLite3
- 同步：supabase-py
- Web端：HTML + JavaScript + Supabase JS SDK（纯静态）
- 部署：GitHub Pages

## 目录结构
```
/
├── README.md          # 项目说明
├── pc/                # PC端代码
│   ├── main.py        # 主程序
│   ├── db.py          # 数据库操作
│   ├── sync.py        # 云端同步
│   └── requirements.txt  # 依赖文件
├── web/               # Web端代码
│   ├── index.html     # 静态页面
│   ├── app.js         # JavaScript功能
│   └── style.css      # 样式文件
└── sql/               # SQL脚本
    └── init.sql       # 数据库初始化
```

## 安装与运行

### PC端
1. 安装依赖：
   ```bash
   pip install -r pc/requirements.txt
   ```
   注意：如果遇到`sync.py`模块导入错误，可能是因为supabase库安装失败。此时应用程序会自动降级，基本功能仍然可用，但无法同步到云端。

2. 运行程序：
   ```bash
   python pc/main.py
   ```

### Web端
1. 将`web`文件夹中的文件上传到GitHub仓库
2. 开启GitHub Pages功能
3. 访问生成的URL即可查看健康记录和进行互动

## 功能使用

### PC端
- **事件记录**：选择事件类型，填写相关信息，点击"保存"按钮
- **统计分析**：使用"今天"、"昨天"、"本周"、"本月"快捷按钮查看统计数据
- **云端同步**：点击"同步到云端"按钮将数据同步到Supabase
- **软删除**：选择要删除的事件，点击"软删除"按钮

### Web端
- **查看记录**：页面会自动加载最新的健康记录
- **访客互动**：选择互动类型（知晓/赞/担心/请回复），输入姓名，点击"提交"按钮
- **互动记录**：页面会显示最新的访客互动记录

## 数据库结构

### 本地SQLite
- `event_records`：事件记录表
- `visitor_interact`：访客互动表

### 云端Supabase
- `event_records`：事件记录表
- `visitor_interact`：访客互动表

## Supabase配置
- Project URL: https://iwpnajbmceobbkvwqtmy.supabase.co
- Anon Key: sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT

## 注意事项
- Web端为纯静态文件，完全符合GitHub Pages的托管要求
- 手机浏览器完美适配，支持随时随地查看和互动
- 本地数据存储在SQLite数据库中，确保数据安全
- 云端同步功能需要安装supabase库才能使用

## 开发说明
本项目按照编写说明.mk的要求开发，实现了所有指定的功能。PC端使用PyQt5构建GUI界面，Web端使用纯HTML+JavaScript实现静态页面。
