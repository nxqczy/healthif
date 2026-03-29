个人作息健康记录系统
（Trae Solo 专用・GitHub 静态部署版）
1. 项目说明
PC 端为主，本地数据库使用 SQLite
云端使用 Supabase 存储
Web 端为纯静态页面，可直接部署在 GitHub Pages
无需服务器，无需后端，GitHub 直接托管可用
单人使用，无登录
支持事件：吃饭、小便、大便、打针、输液、抽血、检查、其他事项
统计支持：昨天、今天、本周、本月 快捷按钮
Web 访客可互动：知晓 / 赞 / 担心 / 请回复 + 填写姓名
2. 技术栈
PC：Python + PyQt5 + SQLite3
同步：supabase-py
Web：HTML + JavaScript + Supabase JS SDK（纯静态）
部署：GitHub Pages（静态托管，完全支持）
3. 本地数据库（SQLite）
CREATE TABLE IF NOT EXISTS event_records (
    id TEXT PRIMARY KEY,
    event_type TEXT NOT NULL,
    other_content TEXT,
    remark TEXT,
    record_date TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    is_deleted INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS visitor_interact (
    id TEXT PRIMARY KEY,
    visitor_name TEXT NOT NULL,
    interact_type TEXT NOT NULL,
    interact_time TEXT NOT NULL,
    note TEXT
);

4. 云端数据库（Supabase）
create extension if not exists "uuid-ossp";

create table event_records (
  id uuid primary key default uuid_generate_v4(),
  event_type text not null,
  other_content text,
  remark text,
  record_date date not null,
  created_at timestamptz default now(),
  updated_at timestamptz default now(),
  is_deleted boolean default false
);

create table visitor_interact (
  id uuid primary key default uuid_generate_v4(),
  visitor_name text not null,
  interact_type text not null,
  interact_time timestamptz default now(),
  note text default ''
);
5. PC 端功能（PyQt5）
5.1 界面结构
事件选择下拉框
其他事项输入框
备注编辑框
保存按钮
软删除按钮
记录列表
统计区域
快捷按钮：昨天、今天、本周、本月
统计结果展示
云端同步按钮
访客互动记录展示区
5.2 统计规则
昨天：自动筛选昨日所有记录
今天：自动筛选今日所有记录
本周：自动筛选本周一至当前
本月：自动筛选当月 1 日至月末
5.3 同步规则
本地 SQLite 为主库
按 UUID + updated_at 时间戳同步
软删除不同步物理删除
PC 上传 → 云端下载合并
6. Web 端（纯静态，GitHub 直接可用）
6.1 功能
查看事件记录
访客互动按钮：知晓 / 赞 / 担心 / 请回复
姓名输入（必填）
提交互动到 Supabase
展示最新互动列表
6.2 技术特点
纯 HTML + JS，无后端
直接放在 GitHub 仓库 docs/ 或 web/ 文件夹
开启 GitHub Pages 即可访问
手机浏览器完美适配
100% 符合 GitHub 静态托管规则
7. GitHub 目录结构
plaintext
/
├── README.md
├── pc/
│   ├── main.py
│   ├── db.py       # SQLite
│   ├── sync.py     # Supabase 同步
│   └── requirements.txt
├── web/
│   ├── index.html  # 静态页面
│   ├── app.js      # 访问 Supabase
│   └── style.css
└── sql/
    └── init.sql
8. PC 依赖
plaintext
PyQt5==5.15.10
supabase==2.3.2
9. Trae Solo 生成指令
plaintext
根据本 spec.md 完整生成项目：
1. PC 端使用 PyQt5 + SQLite 本地数据库
2. 统计界面增加快捷按钮：昨天、今天、本周、本月
3. 增加云端同步按钮，按 updated_at 时间戳同步
4. Web 端为纯静态 HTML+JS，可直接部署 GitHub Pages
5. 实现访客互动：知晓、赞、担心、请回复 + 姓名
6. 代码可直接运行，无需额外配置
我再给你一句最关键的保证（你最关心的）
Web 端只用 HTML + JS，完全是静态文件，GitHub Pages 天然支持，打开就能用，不需要任何服务器，不需要后端，不需要域名额外配置。

我的supabase 配置信息是：
Supabase 连接信息：
- Project URL: https://iwpnajbmceobbkvwqtmy.supabase.co
- Anon Key: sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT


