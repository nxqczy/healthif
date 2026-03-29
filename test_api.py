import requests

# Supabase配置
supabase_url = 'https://iwpnajbmceobbkvwqtmy.supabase.co'
supabase_key = 'sb_publishable_-FWZBtjD8_JcgoaupQSq0w_2KCvd-FT'

# 测试保存事件
def test_save_event():
    url = f"{supabase_url}/rest/v1/event_records"
    headers = {
        'apikey': supabase_key,
        'Authorization': f'Bearer {supabase_key}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }
    import datetime
    now = datetime.datetime.now().isoformat()
    data = {
        'event_type': '测试',
        'other_content': None,
        'remark': '测试',
        'record_date': now,
        'created_at': now,
        'updated_at': now,
        'is_deleted': False
    }
    
    print('测试保存事件...')
    print(f'URL: {url}')
    print(f'Headers: {headers}')
    print(f'Data: {data}')
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f'Response status: {response.status_code}')
        print(f'Response headers: {dict(response.headers)}')
        print(f'Response content: {response.text}')
        
        if response.status_code == 201:
            print('保存成功！')
        else:
            print('保存失败！')
    except Exception as e:
        print(f'请求出错: {e}')

if __name__ == '__main__':
    test_save_event()
