-- 本地SQLite数据库初始化脚本

-- 创建事件记录表
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

-- 创建访客互动表
CREATE TABLE IF NOT EXISTS visitor_interact (
    id TEXT PRIMARY KEY,
    visitor_name TEXT NOT NULL,
    interact_type TEXT NOT NULL,
    interact_time TEXT NOT NULL,
    note TEXT
);

-- 云端Supabase数据库初始化脚本
-- create extension if not exists "uuid-ossp";

-- create table event_records (
--   id uuid primary key default uuid_generate_v4(),
--   event_type text not null,
--   other_content text,
--   remark text,
--   record_date date not null,
--   created_at timestamptz default now(),
--   updated_at timestamptz default now(),
--   is_deleted boolean default false
-- );

-- create table visitor_interact (
--   id uuid primary key default uuid_generate_v4(),
--   visitor_name text not null,
--   interact_type text not null,
--   interact_time timestamptz default now(),
--   note text default ''
-- );
