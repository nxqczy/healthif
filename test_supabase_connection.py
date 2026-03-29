import requests
import json

# Supabase配置
supabase_url = "https://iwpnajbmceobbkvwqtmy.supabase.co"
supabase_key = "sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT"

# 测试连接
print("测试Supabase连接...")
print(f"URL: {supabase_url}")
print(f"Key: {supabase_key}")

# 测试headers
headers = {
    'apikey': supabase_key,
    'Authorization': f'Bearer {supabase_key}',
    'Content-Type': 'application/json'
}
print(f"Headers: {headers}")

# 测试获取事件记录
print("\n测试获取事件记录...")
try:
    response = requests.get(f"{supabase_url}/rest/v1/event_records", headers=headers)
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
except Exception as e:
    print(f"请求失败: {e}")

# 测试获取访客互动记录
print("\n测试获取访客互动记录...")
try:
    response = requests.get(f"{supabase_url}/rest/v1/visitor_interact", headers=headers)
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
except Exception as e:
    print(f"请求失败: {e}")

# 测试插入事件记录
print("\n测试插入事件记录...")
try:
    test_data = {
        'id': 'test-123',
        'event_type': '测试',
        'other_content': None,
        'remark': '测试记录',
        'record_date': '2026-03-29T12:00:00',
        'created_at': '2026-03-29T12:00:00',
        'updated_at': '2026-03-29T12:00:00',
        'is_deleted': False
    }
    response = requests.post(f"{supabase_url}/rest/v1/event_records", headers=headers, data=json.dumps(test_data))
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
except Exception as e:
    print(f"请求失败: {e}")
