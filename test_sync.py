import sys
import os

# 添加pc目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'pc'))

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
