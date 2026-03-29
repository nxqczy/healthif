-- Supabase数据库初始化脚本

-- 启用UUID扩展
create extension if not exists "uuid-ossp";

-- 创建事件记录表
create table event_records (
  id uuid primary key default uuid_generate_v4(),
  event_type text not null,
  other_content text,
  remark text,
  record_date timestamp with time zone not null,
  created_at timestamp with time zone default now(),
  updated_at timestamp with time zone default now(),
  is_deleted boolean default false
);

-- 创建访客互动表
create table visitor_interact (
  id uuid primary key default uuid_generate_v4(),
  visitor_name text not null,
  interact_type text not null,
  interact_time timestamp with time zone default now(),
  note text default ''
);

-- 创建索引以提高查询性能
create index idx_event_records_record_date on event_records(record_date);
create index idx_event_records_is_deleted on event_records(is_deleted);
create index idx_visitor_interact_interact_time on visitor_interact(interact_time);
