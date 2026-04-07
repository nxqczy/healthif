import requests
import json
from datetime import datetime

class SyncManager:
    def __init__(self, url, key, db):
        self.supabase_url = url
        self.supabase_key = key
        self.db = db
        self.headers = {
            'apikey': self.supabase_key,
            'Authorization': f'Bearer {self.supabase_key}',
            'Content-Type': 'application/json'
        }
    
    def sync_to_cloud(self):
        """将本地数据同步到云端"""
        try:
            # 测试连接
            test_response = requests.get(f"{self.supabase_url}/rest/v1/event_records", headers=self.headers, timeout=10)
            print(f"测试连接状态码: {test_response.status_code}")
            
            # 从云端获取所有事件记录
            cloud_events = self.get_events_from_cloud()
            print(f"从云端获取到 {len(cloud_events)} 条事件记录")
            cloud_event_ids = [event['id'] for event in cloud_events]
            
            # 获取本地所有未删除的事件记录
            local_events = self.db.get_all_events()
            print(f"本地事件记录数量: {len(local_events)}")
            local_event_ids = [event['id'] for event in local_events]
            
            # 同步本地事件记录到云端
            synced_count = 0
            for event in local_events:
                if event['id'] not in cloud_event_ids:
                    if self.insert_event_to_cloud(event):
                        synced_count += 1
            
            # 处理本地存在但云端已删除的记录
            for event_id in local_event_ids:
                if event_id not in cloud_event_ids:
                    # 软删除本地记录
                    self.db.soft_delete_event(event_id)
                    print(f"软删除本地事件记录: {event_id}")
            
            print(f"成功同步 {synced_count} 条事件记录到云端")
            
            # 从云端获取访客互动记录
            cloud_interactions = self.get_visitor_interactions_from_cloud()
            print(f"从云端获取到 {len(cloud_interactions)} 条互动记录")
            cloud_interaction_ids = [interaction['id'] for interaction in cloud_interactions]
            
            # 获取本地所有互动记录
            local_interactions = self.db.get_visitor_interactions()
            local_interaction_ids = [interaction['id'] for interaction in local_interactions]
            
            # 将云端互动记录同步到本地
            for interaction in cloud_interactions:
                if interaction['id'] not in local_interaction_ids:
                    # 插入新互动记录到本地
                    self.db.add_visitor_interaction(
                        visitor_name=interaction['visitor_name'],
                        interact_type=interaction['interact_type'],
                        note=interaction.get('note')
                    )
                    print(f"添加新互动记录: {interaction['id']}")
            
            # 处理本地存在但云端已删除的互动记录
            # 注意：由于visitor_interact表没有is_deleted字段，我们需要手动删除
            # 这里简单处理，先删除所有本地互动记录，然后重新从云端同步
            # 实际应用中可能需要更复杂的逻辑
            if len(cloud_interactions) > 0:
                # 这里可以添加删除本地互动记录的逻辑
                pass
            
            return True, f"同步成功，共同步 {synced_count} 条记录"
        except Exception as e:
            print(f"同步失败: {str(e)}")
            return False, f"同步失败: {str(e)}"
    
    def get_visitor_interactions_from_cloud(self):
        """从云端获取所有访客互动记录"""
        url = f"{self.supabase_url}/rest/v1/visitor_interact"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return data
            else:
                return []
        except Exception as e:
            print(f"从云端获取访客互动记录失败: {e}")
            return []
    
    def get_events_from_cloud(self):
        """从云端获取所有事件记录"""
        url = f"{self.supabase_url}/rest/v1/event_records"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                return data
            else:
                return []
        except Exception as e:
            print(f"从云端获取事件记录失败: {e}")
            return []
    
    def insert_event_to_cloud(self, event):
        """插入事件记录到云端"""
        try:
            # 转换时间格式为ISO格式
            def convert_to_iso(time_str):
                try:
                    # 解析本地时间格式（YYYY-MM-DD HH:MM:SS）
                    dt = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                    # 转换为ISO格式
                    return dt.isoformat()
                except Exception as e:
                    print(f"时间格式转换失败: {e}")
                    return time_str
            
            # 准备数据
            event_data = {
                'id': event['id'],
                'event_type': event['event_type'],
                'other_content': event['other_content'],
                'remark': event['remark'],
                'record_date': convert_to_iso(event['record_date']),
                'created_at': convert_to_iso(event['created_at']),
                'updated_at': convert_to_iso(event['updated_at']),
                'is_deleted': event['is_deleted'] == 1
            }
            
            # 插入数据
            url = f"{self.supabase_url}/rest/v1/event_records"
            response = requests.post(url, headers=self.headers, data=json.dumps(event_data), timeout=10)
            
            if response.status_code == 201:
                print(f"成功插入事件记录: {event['id']}")
                return True
            else:
                print(f"插入失败，状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                return False
        except Exception as e:
            print(f"插入事件记录失败: {e}")
            return False

