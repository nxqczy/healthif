import sqlite3
import uuid
from datetime import datetime, timedelta

class Database:
    def __init__(self, db_path='health_record.db'):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """初始化数据库，创建表结构"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # 创建事件记录表
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS event_records (
                id TEXT PRIMARY KEY,
                event_type TEXT NOT NULL,
                other_content TEXT,
                remark TEXT,
                record_date TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                is_deleted INTEGER DEFAULT 0
            )
            ''')
            # 创建访客互动表
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS visitor_interact (
                id TEXT PRIMARY KEY,
                visitor_name TEXT NOT NULL,
                interact_type TEXT NOT NULL,
                interact_time TEXT NOT NULL,
                note TEXT
            )
            ''')
            conn.commit()
    
    def add_event(self, event_type, other_content=None, remark=None):
        """添加事件记录"""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record = {
            'id': str(uuid.uuid4()),
            'event_type': event_type,
            'other_content': other_content,
            'remark': remark,
            'record_date': now,
            'created_at': now,
            'updated_at': now,
            'is_deleted': 0
        }
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO event_records (id, event_type, other_content, remark, record_date, created_at, updated_at, is_deleted)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (record['id'], record['event_type'], record['other_content'], record['remark'],
                  record['record_date'], record['created_at'], record['updated_at'], record['is_deleted']))
            conn.commit()
        return record
    
    def get_events(self, start_date=None, end_date=None):
        """获取事件记录，支持时间范围查询"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = 'SELECT * FROM event_records WHERE is_deleted = 0'
            params = []
            
            if start_date and end_date:
                query += ' AND record_date >= ? AND record_date <= ?'
                params.extend([start_date, end_date])
            
            query += ' ORDER BY record_date DESC'
            
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def soft_delete_event(self, event_id):
        """软删除事件记录"""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE event_records SET is_deleted = 1, updated_at = ? WHERE id = ?
            ''', (now, event_id))
            conn.commit()
        return cursor.rowcount > 0
    
    def get_events_by_time_range(self, time_range):
        """根据时间范围获取事件记录"""
        now = datetime.now()
        
        if time_range == 'today':
            start_date = now.strftime('%Y-%m-%d 00:00:00')
            end_date = now.strftime('%Y-%m-%d 23:59:59')
        elif time_range == 'yesterday':
            yesterday = now - timedelta(days=1)
            start_date = yesterday.strftime('%Y-%m-%d 00:00:00')
            end_date = yesterday.strftime('%Y-%m-%d 23:59:59')
        elif time_range == 'this_week':
            # 获取本周一
            monday = now - timedelta(days=now.weekday())
            start_date = monday.strftime('%Y-%m-%d 00:00:00')
            end_date = now.strftime('%Y-%m-%d 23:59:59')
        elif time_range == 'this_month':
            # 获取本月1号
            first_day = now.replace(day=1)
            start_date = first_day.strftime('%Y-%m-%d 00:00:00')
            # 计算本月最后一天
            if now.month == 12:
                last_day = now.replace(year=now.year+1, month=1, day=1) - timedelta(days=1)
            else:
                last_day = now.replace(month=now.month+1, day=1) - timedelta(days=1)
            end_date = last_day.strftime('%Y-%m-%d 23:59:59')
        else:
            return []
        
        return self.get_events(start_date, end_date)
    
    def get_all_events(self):
        """获取所有未删除的事件记录"""
        return self.get_events()
    
    def get_visitor_interactions(self):
        """获取访客互动记录"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM visitor_interact ORDER BY interact_time DESC')
            return [dict(row) for row in cursor.fetchall()]
    
    def add_visitor_interaction(self, visitor_name, interact_type, note=None):
        """添加访客互动记录"""
        now = datetime.now().isoformat()
        interaction = {
            'id': str(uuid.uuid4()),
            'visitor_name': visitor_name,
            'interact_type': interact_type,
            'interact_time': now,
            'note': note
        }
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO visitor_interact (id, visitor_name, interact_type, interact_time, note)
            VALUES (?, ?, ?, ?, ?)
            ''', (interaction['id'], interaction['visitor_name'], interaction['interact_type'],
                  interaction['interact_time'], interaction['note']))
            conn.commit()
        return interaction
