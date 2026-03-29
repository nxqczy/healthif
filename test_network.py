import requests

# 测试基本网络连接
print("测试网络连接...")
try:
    response = requests.get("https://www.google.com", timeout=10)
    print(f"Google连接成功，状态码: {response.status_code}")
except Exception as e:
    print(f"网络连接失败: {e}")

# 测试Supabase连接
print("\n测试Supabase连接...")
supabase_url = "https://iwpnajbmceobbkvwqtmy.supabase.co"
try:
    response = requests.get(supabase_url, timeout=10)
    print(f"Supabase连接成功，状态码: {response.status_code}")
except Exception as e:
    print(f"Supabase连接失败: {e}")
