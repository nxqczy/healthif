import requests
import json
import time
from datetime import datetime

class SyncCloud:
    def __init__(self, supabase_url, supabase_key):
        self.supabase_url = supabase_url
        self.supabase_key = supabase_key
        self.headers = {
            'apikey': self.supabase_key,
            'Authorization': f'Bearer {self.supabase_key}',
            'Content-Type': 'application/json'
        }
        # 初始化时创建表结构
        self.create_tables()
    
    def create_tables(self):
        """创建Supabase表结构"""
        print("开始创建Supabase表结构")
        
        # 创建图书表
        self.create_books_table()
        
        # 创建流程架构设计表
        self.create_process_architecture_table()
        
        # 创建流程构建表
        self.create_process_construction_table()
        
        # 创建四级问题库表
        self.create_four_level_question_table()
        
        # 创建问题类别表
        self.create_question_categories_table()
        
        # 创建常见问题表
        self.create_common_questions_table()
        
        # 创建问题描述表
        self.create_problem_descriptions_table()
        
        print("Supabase表结构创建完成")
    
    def create_books_table(self):
        """创建图书表"""
        url = f"{self.supabase_url}/rest/v1/books"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'book_uuid': 'test_uuid',
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '978-0-000-00000-0',
            'update_time': int(time.time()),
            'is_deleted': False,
            'summary': 'Test summary',
            'process_domain': 'Test domain',
            'process_group': 'Test group',
            'maturity_level': 1,
            'material_property': 'Test property'
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试图书表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("图书表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE books (
                    id INTEGER PRIMARY KEY,
                    book_uuid TEXT UNIQUE NOT NULL,
                    title TEXT,
                    author TEXT,
                    isbn TEXT,
                    update_time INTEGER,
                    is_deleted BOOLEAN DEFAULT false,
                    summary TEXT,
                    process_domain TEXT,
                    process_group TEXT,
                    maturity_level INTEGER,
                    material_property TEXT
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("图书表存在，表结构正确")
            else:
                print(f"图书表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试图书表失败: {e}")
            import traceback
            traceback.print_exc()

    def create_process_architecture_table(self):
        """创建流程架构设计表"""
        url = f"{self.supabase_url}/rest/v1/process_architecture_design"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'item_uuid': 'test_uuid',
            'serial_num': 'test',
            'arch_design_example': 'test',
            'example_character': 'test',
            'arch_advantages': 'test',
            'advantage_type': 'test',
            'exist_problem': 'test',
            'problem_type': 'test',
            'enlightenment': 'test',
            'create_time': datetime.now().isoformat(),
            'update_time': int(time.time()),
            'is_deleted': False
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试流程架构设计表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("流程架构设计表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE process_architecture_design (
                    id INTEGER PRIMARY KEY,
                    item_uuid TEXT UNIQUE NOT NULL,
                    serial_num TEXT NOT NULL,
                    arch_design_example TEXT,
                    example_character TEXT NOT NULL,
                    arch_advantages TEXT NOT NULL,
                    advantage_type TEXT NOT NULL,
                    exist_problem TEXT NOT NULL,
                    problem_type TEXT NOT NULL,
                    enlightenment TEXT,
                    create_time TEXT NOT NULL,
                    update_time INTEGER,
                    is_deleted BOOLEAN DEFAULT false
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("流程架构设计表存在，表结构正确")
            else:
                print(f"流程架构设计表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试流程架构设计表失败: {e}")
            import traceback
            traceback.print_exc()
    
    def create_process_construction_table(self):
        """创建流程构建表"""
        url = f"{self.supabase_url}/rest/v1/process_construction"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'item_uuid': 'test_uuid',
            'serial_num': 'test',
            'process_common_problem': 'test',
            'problem_detail': 'test',
            'ideal_model_example': 'test',
            'create_time': datetime.now().isoformat(),
            'update_time': int(time.time()),
            'is_deleted': False
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试流程构建表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("流程构建表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE process_construction (
                    id INTEGER PRIMARY KEY,
                    item_uuid TEXT UNIQUE NOT NULL,
                    serial_num TEXT NOT NULL,
                    process_common_problem TEXT NOT NULL,
                    problem_detail TEXT,
                    ideal_model_example TEXT,
                    create_time TEXT NOT NULL,
                    update_time INTEGER,
                    is_deleted BOOLEAN DEFAULT false
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("流程构建表存在，表结构正确")
            else:
                print(f"流程构建表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试流程构建表失败: {e}")
            import traceback
            traceback.print_exc()
    
    def create_four_level_question_table(self):
        """创建四级问题库表"""
        url = f"{self.supabase_url}/rest/v1/four_level_question_library"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'item_uuid': 'test_uuid',
            'question_category': 'test',
            'common_question': 'test',
            'problem_description': 'test',
            'specific_performance': 'test',
            'measure_example': 'test',
            'create_time': datetime.now().isoformat(),
            'update_time': int(time.time()),
            'is_deleted': False
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试四级问题库表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("四级问题库表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE four_level_question_library (
                    id INTEGER PRIMARY KEY,
                    item_uuid TEXT UNIQUE NOT NULL,
                    question_category TEXT NOT NULL,
                    common_question TEXT NOT NULL,
                    problem_description TEXT,
                    specific_performance TEXT,
                    measure_example TEXT,
                    create_time TEXT NOT NULL,
                    update_time INTEGER,
                    is_deleted BOOLEAN DEFAULT false
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("四级问题库表存在，表结构正确")
            else:
                print(f"四级问题库表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试四级问题库表失败: {e}")
            import traceback
            traceback.print_exc()
    
    def create_question_categories_table(self):
        """创建问题类别表"""
        url = f"{self.supabase_url}/rest/v1/question_categories"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'name': 'test',
            'create_time': datetime.now().isoformat(),
            'update_time': datetime.now().isoformat()
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试问题类别表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("问题类别表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE question_categories (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL UNIQUE,
                    create_time TEXT NOT NULL,
                    update_time TEXT NOT NULL
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("问题类别表存在，表结构正确")
            else:
                print(f"问题类别表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试问题类别表失败: {e}")
            import traceback
            traceback.print_exc()
    
    def create_common_questions_table(self):
        """创建常见问题表"""
        url = f"{self.supabase_url}/rest/v1/common_questions"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'category_name': 'test',
            'name': 'test',
            'create_time': datetime.now().isoformat(),
            'update_time': datetime.now().isoformat()
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试常见问题表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("常见问题表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE common_questions (
                    id INTEGER PRIMARY KEY,
                    category_name TEXT NOT NULL,
                    name TEXT NOT NULL,
                    create_time TEXT NOT NULL,
                    update_time TEXT NOT NULL
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("常见问题表存在，表结构正确")
            else:
                print(f"常见问题表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试常见问题表失败: {e}")
            import traceback
            traceback.print_exc()
    
    def create_problem_descriptions_table(self):
        """创建问题描述表"""
        url = f"{self.supabase_url}/rest/v1/problem_descriptions"
        # 尝试插入一条数据，如果表不存在，会返回错误
        test_data = {
            'id': 0,
            'question_name': 'test',
            'description': 'test',
            'create_time': datetime.now().isoformat(),
            'update_time': datetime.now().isoformat()
        }
        
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(test_data))
            print(f"测试问题描述表: 状态码={response.status_code}, 响应={response.text}")
            if response.status_code == 404:
                # 表不存在，需要创建
                print("问题描述表不存在，需要在Supabase中手动创建")
                print("请在Supabase控制台执行以下SQL语句创建表:")
                print("""
                CREATE TABLE problem_descriptions (
                    id INTEGER PRIMARY KEY,
                    question_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    create_time TEXT NOT NULL,
                    update_time TEXT NOT NULL
                );
                """)
            elif response.status_code == 201:
                # 表存在，删除测试数据
                delete_response = requests.delete(f"{url}?id=eq.0", headers=self.headers)
                print(f"删除测试数据: 状态码={delete_response.status_code}")
            elif response.status_code == 422:
                # 表存在，但数据验证失败，说明表结构正确
                print("问题描述表存在，表结构正确")
            else:
                print(f"问题描述表测试失败: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"测试问题描述表失败: {e}")
            import traceback
            traceback.print_exc()
    
    def get_books_from_cloud(self):
        """从云端获取所有图书数据"""
        url = f"{self.supabase_url}/rest/v1/books"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            # 确保返回的数据是列表格式
            if isinstance(data, list):
                # 处理每条记录，确保字段完整
                for book in data:
                    # 确保必要字段存在
                    if 'book_uuid' not in book:
                        continue
                    # 确保update_time是整数类型
                    if 'update_time' in book:
                        try:
                            book['update_time'] = int(book['update_time'])
                        except (ValueError, TypeError):
                            book['update_time'] = 0
                    else:
                        book['update_time'] = 0
                    # 确保is_deleted是布尔类型
                    if 'is_deleted' not in book:
                        book['is_deleted'] = False
                    # 确保其他字段存在
                    for field in ['title', 'author', 'isbn', 'summary', 'process_domain', 'process_group', 'maturity_level', 'material_property']:
                        if field not in book:
                            book[field] = '' if field != 'maturity_level' else None
                return data
            else:
                print(f"云端返回的数据格式错误: {type(data)}")
                return []
        except Exception as e:
            print(f"从云端获取数据失败: {e}")
            return []
    
    def upsert_book_to_cloud(self, book_data):
        """上传图书数据到云端"""
        # 只上传轻量字段
        light_data = {
            'book_uuid': book_data['book_uuid'],
            'title': book_data['title'],
            'author': book_data['author'],
            'isbn': book_data['isbn'],
            'summary': book_data.get('summary', ''),
            'process_domain': book_data.get('process_domain', ''),
            'process_group': book_data.get('process_group', ''),
            'maturity_level': book_data.get('maturity_level'),
            'material_property': book_data.get('material_property', ''),
            'update_time': book_data['update_time'],
            'is_deleted': book_data['is_deleted']
        }
        
        print(f"准备上传数据: {light_data}")
        
        # 先尝试更新数据
        update_url = f"{self.supabase_url}/rest/v1/books"
        update_headers = {**self.headers, 'Prefer': 'return=representation'}
        update_data = light_data.copy()
        book_uuid = update_data.pop('book_uuid')
        
        try:
            # 尝试更新现有记录
            print(f"尝试更新记录: {book_uuid}")
            response = requests.patch(
                f"{update_url}?book_uuid=eq.{book_uuid}",
                headers=update_headers,
                data=json.dumps(update_data)
            )
            
            print(f"更新响应状态码: {response.status_code}")
            print(f"更新响应内容: {response.text}")
            
            if response.status_code == 200:
                # 检查响应内容是否为空
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    # 更新成功
                    print(f"成功更新数据: {book_uuid} - {book_data['title']}")
                    return True
                else:
                    # 响应为空，可能更新失败
                    print(f"更新响应为空，尝试插入: {book_uuid} - {book_data['title']}")
            elif response.status_code == 404:
                # 记录不存在，尝试插入
                print(f"记录不存在，尝试插入: {book_uuid} - {book_data['title']}")
            
            # 尝试插入新记录
            print(f"尝试插入新记录: {book_uuid} - {book_data['title']}")
            insert_url = f"{self.supabase_url}/rest/v1/books"
            insert_response = requests.post(
                insert_url,
                headers=update_headers,
                data=json.dumps(light_data)
            )
            
            print(f"插入响应状态码: {insert_response.status_code}")
            print(f"插入响应内容: {insert_response.text}")
            
            if insert_response.status_code == 201:
                # 插入成功
                print(f"成功插入数据: {book_uuid} - {book_data['title']}")
                return True
            else:
                # 插入失败
                insert_response.raise_for_status()
        except Exception as e:
            print(f"上传数据失败: {e}")
            # 如果更新/插入失败，尝试先删除再插入
            try:
                print(f"尝试先删除再插入: {book_uuid} - {book_data['title']}")
                # 先删除
                delete_response = requests.delete(
                    f"{update_url}?book_uuid=eq.{book_uuid}",
                    headers=self.headers
                )
                print(f"删除响应状态码: {delete_response.status_code}")
                
                # 再插入
                insert_response = requests.post(
                    f"{self.supabase_url}/rest/v1/books",
                    headers={**self.headers, 'Prefer': 'return=representation'},
                    data=json.dumps(light_data)
                )
                
                print(f"删除后插入响应状态码: {insert_response.status_code}")
                print(f"删除后插入响应内容: {insert_response.text}")
                
                if insert_response.status_code == 201:
                    print(f"成功删除并插入数据: {book_uuid} - {book_data['title']}")
                    return True
                else:
                    insert_response.raise_for_status()
            except Exception as e2:
                print(f"删除并插入失败: {e2}")
                return False
    
    def sync_to_cloud(self, local_books):
        """将本地数据同步到云端"""
        print(f"开始同步到云端，本地图书数量: {len(local_books)}")
        cloud_books = self.get_books_from_cloud()
        print(f"从云端获取的图书数量: {len(cloud_books)}")
        cloud_books_dict = {book['book_uuid']: book for book in cloud_books}
        
        synced_count = 0
        for book in local_books:
            book_uuid, title, author, isbn, summary, process_domain, process_group, maturity_level, material_property, update_time, is_deleted = book
            print(f"处理本地图书: {book_uuid} - {title}, 更新时间: {update_time}")
            book_data = {
                'book_uuid': book_uuid,
                'title': title,
                'author': author,
                'isbn': isbn,
                'summary': summary,
                'process_domain': process_domain,
                'process_group': process_group,
                'maturity_level': maturity_level,
                'material_property': material_property,
                'update_time': update_time,
                'is_deleted': bool(is_deleted)
            }
            
            # 检查云端是否存在
            if book_uuid in cloud_books_dict:
                cloud_book = cloud_books_dict[book_uuid]
                print(f"云端存在该图书: {cloud_book['title']}, 更新时间: {cloud_book.get('update_time', 0)}")
                # 只在本地数据更新时间较新时同步
                try:
                    cloud_update_time = int(cloud_book.get('update_time', 0))
                    print(f"本地时间: {update_time}, 云端时间: {cloud_update_time}")
                    if update_time > cloud_update_time:
                        print(f"本地数据较新，需要同步")
                        if self.upsert_book_to_cloud(book_data):
                            print(f"更新云端数据: {book_uuid} - {title}")
                            synced_count += 1
                    else:
                        print(f"本地数据不是最新，跳过同步")
                except (ValueError, TypeError) as e:
                    print(f"时间格式错误: {e}")
                    # 如果云端时间格式不正确，直接同步
                    if self.upsert_book_to_cloud(book_data):
                        print(f"更新云端数据 (时间格式错误): {book_uuid} - {title}")
                        synced_count += 1
            else:
                print(f"云端不存在该图书，需要新增")
                # 云端不存在，新增
                if self.upsert_book_to_cloud(book_data):
                    print(f"新增云端数据: {book_uuid} - {title}")
                    synced_count += 1
        
        print(f"同步到云端完成，同步数量: {synced_count}")
        return synced_count
    
    def sync_from_cloud(self, db):
        """从云端同步数据到本地"""
        cloud_books = self.get_books_from_cloud()
        print(f"开始从云端同步，云端图书数量: {len(cloud_books)}")
        local_books = db.get_all_books_for_sync()
        print(f"本地图书数量: {len(local_books)}")
        local_books_dict = {book[0]: book for book in local_books}
        
        synced_count = 0
        for cloud_book in cloud_books:
            book_uuid = cloud_book['book_uuid']
            print(f"处理云端图书: {book_uuid} - {cloud_book['title']}, 更新时间: {cloud_book.get('update_time', 0)}")
            # 检查本地是否存在
            if book_uuid in local_books_dict:
                local_book = local_books_dict[book_uuid]
                print(f"本地存在该图书: {local_book[1]}, 更新时间: {local_book[9]}")
                # 只在云端数据更新时间较新时同步
                try:
                    cloud_update_time = int(cloud_book.get('update_time', 0))
                    local_update_time = int(local_book[9])  # 本地更新时间在索引9
                    print(f"云端时间: {cloud_update_time}, 本地时间: {local_update_time}")
                    
                    # 严格以时间戳为准
                    if cloud_update_time > local_update_time:
                        print(f"云端数据较新，需要同步")
                        db.update_from_sync(cloud_book)
                        print(f"从云端更新本地数据: {book_uuid} - {cloud_book['title']}")
                        synced_count += 1
                    else:
                        print(f"云端数据不是最新，跳过同步")
                except (ValueError, TypeError) as e:
                    print(f"时间格式错误: {e}")
                    # 如果时间格式不正确，直接同步
                    db.update_from_sync(cloud_book)
                    print(f"从云端更新本地数据 (时间格式错误): {book_uuid} - {cloud_book['title']}")
                    synced_count += 1
            else:
                print(f"本地不存在该图书，需要新增")
                # 本地不存在，新增
                db.update_from_sync(cloud_book)
                print(f"从云端新增本地数据: {book_uuid} - {cloud_book['title']}")
                synced_count += 1
        
        print(f"从云端同步完成，同步数量: {synced_count}")
        return synced_count
    
    def full_sync(self, db):
        """执行完整同步：先从云端同步，再同步到云端"""
        print("开始同步...")
        print("1. 从云端同步到本地")
        from_cloud_count = self.sync_from_cloud(db)
        print(f"从云端同步了 {from_cloud_count} 条数据")
        
        print("2. 从本地同步到云端")
        local_books = db.get_all_books_for_sync()
        to_cloud_count = self.sync_to_cloud(local_books)
        print(f"同步到云端 {to_cloud_count} 条数据")
        
        print(f"同步完成，共同步 {from_cloud_count + to_cloud_count} 条数据")
        return from_cloud_count + to_cloud_count
    
    # ==================== 流程体系建设管理系统同步方法 ====================
    
    # ========== 流程架构设计同步 ==========
    def get_process_architecture_from_cloud(self):
        """从云端获取所有流程架构设计数据"""
        url = f"{self.supabase_url}/rest/v1/process_architecture_design"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                for item in data:
                    if 'item_uuid' not in item:
                        continue
                    if 'update_time' in item:
                        try:
                            item['update_time'] = int(item['update_time'])
                        except (ValueError, TypeError):
                            item['update_time'] = 0
                    else:
                        item['update_time'] = 0
                    if 'is_deleted' not in item:
                        item['is_deleted'] = False
                return data
            else:
                print(f"云端返回的数据格式错误: {type(data)}")
                return []
        except Exception as e:
            print(f"从云端获取流程架构设计失败: {e}")
            return []
    
    def upsert_process_architecture_to_cloud(self, data):
        """上传流程架构设计数据到云端"""
        # 为id字段生成唯一值（使用UUID的哈希值）
        import hashlib
        id_value = int(hashlib.md5(data['item_uuid'].encode()).hexdigest(), 16) % 1000000
        
        light_data = {
            'id': id_value,
            'item_uuid': data['item_uuid'],
            'serial_num': data['serial_num'],
            'arch_design_example': data.get('arch_design_example', ''),
            'example_character': data['example_character'],
            'arch_advantages': data['arch_advantages'],
            'advantage_type': data['advantage_type'],
            'exist_problem': data['exist_problem'],
            'problem_type': data['problem_type'],
            'enlightenment': data.get('enlightenment', ''),
            'create_time': data.get('create_time', datetime.now().isoformat()),
            'update_time': data['update_time'],
            'is_deleted': data.get('is_deleted', False)
        }
        
        update_url = f"{self.supabase_url}/rest/v1/process_architecture_design"
        update_headers = {**self.headers, 'Prefer': 'return=representation'}
        update_data = light_data.copy()
        item_uuid = update_data.pop('item_uuid')
        
        try:
            response = requests.patch(
                f"{update_url}?item_uuid=eq.{item_uuid}",
                headers=update_headers,
                data=json.dumps(update_data)
            )
            
            if response.status_code == 200:
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    print(f"成功更新流程架构设计: {item_uuid}")
                    return True
            
            response = requests.post(update_url, headers=update_headers, data=json.dumps(light_data))
            
            if response.status_code == 201:
                print(f"成功插入流程架构设计: {item_uuid}")
                return True
            else:
                print(f"上传失败状态码: {response.status_code}")
                print(f"上传失败响应: {response.text}")
                response.raise_for_status()
        except Exception as e:
            print(f"上传流程架构设计失败: {e}")
            try:
                requests.delete(f"{update_url}?item_uuid=eq.{item_uuid}", headers=self.headers)
                response = requests.post(update_url, headers=update_headers, data=json.dumps(light_data))
                if response.status_code == 201:
                    return True
                else:
                    print(f"删除后插入失败状态码: {response.status_code}")
                    print(f"删除后插入失败响应: {response.text}")
            except Exception as e2:
                print(f"删除并插入失败: {e2}")
            return False
    
    def sync_process_architecture_to_cloud(self, process_architecture_data):
        """同步流程架构设计数据到云端"""
        print(f"开始同步流程架构设计数据，数量: {len(process_architecture_data)}")
        cloud_data = self.get_process_architecture_from_cloud()
        cloud_dict = {item['item_uuid']: item for item in cloud_data}
        
        synced_count = 0
        for item in process_architecture_data:
            try:
                item_uuid, serial_num, arch_design_example, example_character, arch_advantages, advantage_type, exist_problem, problem_type, enlightenment, create_time, update_time, is_deleted = item
                data = {
                    'item_uuid': item_uuid,
                    'serial_num': serial_num,
                    'arch_design_example': arch_design_example,
                    'example_character': example_character,
                    'arch_advantages': arch_advantages,
                    'advantage_type': advantage_type,
                    'exist_problem': exist_problem,
                    'problem_type': problem_type,
                    'enlightenment': enlightenment,
                    'create_time': create_time or datetime.now().isoformat(),
                    'update_time': update_time,
                    'is_deleted': bool(is_deleted)
                }
                
                if item_uuid in cloud_dict:
                    cloud_item = cloud_dict[item_uuid]
                    try:
                        cloud_update_time = int(cloud_item.get('update_time', 0))
                        if update_time > cloud_update_time:
                            if self.upsert_process_architecture_to_cloud(data):
                                synced_count += 1
                    except:
                        if self.upsert_process_architecture_to_cloud(data):
                            synced_count += 1
                else:
                    if self.upsert_process_architecture_to_cloud(data):
                        synced_count += 1
            except Exception as e:
                print(f"同步流程架构设计数据失败: {e}")
        
        print(f"流程架构设计数据同步完成，同步数量: {synced_count}")
        return synced_count
    
    def sync_process_architecture_from_cloud(self, db):
        """从云端同步流程架构设计到本地"""
        cloud_data = self.get_process_architecture_from_cloud()
        print(f"开始从云端同步流程架构设计，数量: {len(cloud_data)}")
        local_data = db.get_all_process_architecture_for_sync()
        local_dict = {item[0]: item for item in local_data}
        
        synced_count = 0
        for cloud_item in cloud_data:
            item_uuid = cloud_item['item_uuid']
            try:
                if item_uuid in local_dict:
                    local_item = local_dict[item_uuid]
                    try:
                        cloud_update_time = int(cloud_item.get('update_time', 0))
                        local_update_time = int(local_item[9])
                        if cloud_update_time > local_update_time:
                            db.update_process_architecture_from_sync(cloud_item)
                            synced_count += 1
                    except:
                        db.update_process_architecture_from_sync(cloud_item)
                        synced_count += 1
                # 本地不存在的记录，不添加到本地，以本地数据为主
            except Exception as e:
                print(f"同步流程架构设计失败: {e}")
        
        print(f"从云端同步流程架构设计完成，同步数量: {synced_count}")
        return synced_count
    
    # ========== 流程构建同步 ==========
    def get_process_construction_from_cloud(self):
        """从云端获取所有流程构建数据"""
        url = f"{self.supabase_url}/rest/v1/process_construction"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                for item in data:
                    if 'item_uuid' not in item:
                        continue
                    if 'update_time' in item:
                        try:
                            item['update_time'] = int(item['update_time'])
                        except (ValueError, TypeError):
                            item['update_time'] = 0
                    else:
                        item['update_time'] = 0
                    if 'is_deleted' not in item:
                        item['is_deleted'] = False
                return data
            else:
                print(f"云端返回的数据格式错误: {type(data)}")
                return []
        except Exception as e:
            print(f"从云端获取流程构建失败: {e}")
            return []
    
    def upsert_process_construction_to_cloud(self, data):
        """上传流程构建数据到云端"""
        # 为id字段生成唯一值（使用UUID的哈希值）
        import hashlib
        id_value = int(hashlib.md5(data['item_uuid'].encode()).hexdigest(), 16) % 1000000
        
        light_data = {
            'id': id_value,
            'item_uuid': data['item_uuid'],
            'serial_num': data['serial_num'],
            'process_common_problem': data['process_common_problem'],
            'problem_detail': data.get('problem_detail', ''),
            'ideal_model_example': data.get('ideal_model_example', ''),
            'create_time': data.get('create_time', datetime.now().isoformat()),
            'update_time': data['update_time'],
            'is_deleted': data.get('is_deleted', False)
        }
        
        update_url = f"{self.supabase_url}/rest/v1/process_construction"
        update_headers = {**self.headers, 'Prefer': 'return=representation'}
        update_data = light_data.copy()
        item_uuid = update_data.pop('item_uuid')
        
        try:
            response = requests.patch(
                f"{update_url}?item_uuid=eq.{item_uuid}",
                headers=update_headers,
                data=json.dumps(update_data)
            )
            
            if response.status_code == 200:
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    print(f"成功更新流程构建: {item_uuid}")
                    return True
            
            response = requests.post(update_url, headers=update_headers, data=json.dumps(light_data))
            
            if response.status_code == 201:
                print(f"成功插入流程构建: {item_uuid}")
                return True
            else:
                response.raise_for_status()
        except Exception as e:
            print(f"上传流程构建失败: {e}")
            try:
                requests.delete(f"{update_url}?item_uuid=eq.{item_uuid}", headers=self.headers)
                response = requests.post(update_url, headers=update_headers, data=json.dumps(light_data))
                if response.status_code == 201:
                    return True
            except Exception as e2:
                print(f"删除并插入失败: {e2}")
            return False
    
    def sync_process_construction_to_cloud(self, process_construction_data):
        """同步流程构建数据到云端"""
        print(f"开始同步流程构建数据，数量: {len(process_construction_data)}")
        cloud_data = self.get_process_construction_from_cloud()
        cloud_dict = {item['item_uuid']: item for item in cloud_data}
        
        synced_count = 0
        for item in process_construction_data:
            try:
                item_uuid, serial_num, process_common_problem, problem_detail, ideal_model_example, create_time, update_time, is_deleted = item
                data = {
                    'item_uuid': item_uuid,
                    'serial_num': serial_num,
                    'process_common_problem': process_common_problem,
                    'problem_detail': problem_detail,
                    'ideal_model_example': ideal_model_example,
                    'create_time': create_time or datetime.now().isoformat(),
                    'update_time': update_time,
                    'is_deleted': bool(is_deleted)
                }
                
                if item_uuid in cloud_dict:
                    cloud_item = cloud_dict[item_uuid]
                    try:
                        cloud_update_time = int(cloud_item.get('update_time', 0))
                        if update_time > cloud_update_time:
                            if self.upsert_process_construction_to_cloud(data):
                                synced_count += 1
                    except:
                        if self.upsert_process_construction_to_cloud(data):
                            synced_count += 1
                else:
                    if self.upsert_process_construction_to_cloud(data):
                        synced_count += 1
            except Exception as e:
                print(f"同步流程构建数据失败: {e}")
        
        print(f"流程构建数据同步完成，同步数量: {synced_count}")
        return synced_count
    
    def sync_process_construction_from_cloud(self, db):
        """从云端同步流程构建到本地"""
        cloud_data = self.get_process_construction_from_cloud()
        print(f"开始从云端同步流程构建，数量: {len(cloud_data)}")
        local_data = db.get_all_process_construction_for_sync()
        local_dict = {item[0]: item for item in local_data}
        
        synced_count = 0
        for cloud_item in cloud_data:
            item_uuid = cloud_item['item_uuid']
            try:
                if item_uuid in local_dict:
                    local_item = local_dict[item_uuid]
                    try:
                        cloud_update_time = int(cloud_item.get('update_time', 0))
                        local_update_time = int(local_item[6])
                        if cloud_update_time > local_update_time:
                            db.update_process_construction_from_sync(cloud_item)
                            synced_count += 1
                    except:
                        db.update_process_construction_from_sync(cloud_item)
                        synced_count += 1
                # 本地不存在的记录，不添加到本地，以本地数据为主
            except Exception as e:
                print(f"同步流程构建失败: {e}")
        
        print(f"从云端同步流程构建完成，同步数量: {synced_count}")
        return synced_count
    
    # ========== 四级问题库同步 ==========
    def get_four_level_question_from_cloud(self):
        """从云端获取所有四级问题库数据"""
        url = f"{self.supabase_url}/rest/v1/four_level_question_library"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                for item in data:
                    if 'item_uuid' not in item:
                        continue
                    if 'update_time' in item:
                        try:
                            item['update_time'] = int(item['update_time'])
                        except (ValueError, TypeError):
                            item['update_time'] = 0
                    else:
                        item['update_time'] = 0
                    if 'is_deleted' not in item:
                        item['is_deleted'] = False
                return data
            else:
                print(f"云端返回的数据格式错误: {type(data)}")
                return []
        except Exception as e:
            print(f"从云端获取四级问题库失败: {e}")
            return []
    
    def upsert_four_level_question_to_cloud(self, data):
        """上传四级问题库数据到云端"""
        # 为id字段生成唯一值（使用UUID的哈希值）
        import hashlib
        id_value = int(hashlib.md5(data['item_uuid'].encode()).hexdigest(), 16) % 1000000
        
        light_data = {
            'id': id_value,
            'item_uuid': data['item_uuid'],
            'question_category': data['question_category'],
            'common_question': data['common_question'],
            'problem_description': data.get('problem_description', ''),
            'specific_performance': data.get('specific_performance', ''),
            'measure_example': data.get('measure_example', ''),
            'create_time': data.get('create_time', datetime.now().isoformat()),
            'update_time': data['update_time'],
            'is_deleted': data.get('is_deleted', False)
        }
        
        update_url = f"{self.supabase_url}/rest/v1/four_level_question_library"
        update_headers = {**self.headers, 'Prefer': 'return=representation'}
        update_data = light_data.copy()
        item_uuid = update_data.pop('item_uuid')
        
        try:
            response = requests.patch(
                f"{update_url}?item_uuid=eq.{item_uuid}",
                headers=update_headers,
                data=json.dumps(update_data)
            )
            
            if response.status_code == 200:
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    print(f"成功更新四级问题库: {item_uuid}")
                    return True
            
            response = requests.post(update_url, headers=update_headers, data=json.dumps(light_data))
            
            if response.status_code == 201:
                print(f"成功插入四级问题库: {item_uuid}")
                return True
            else:
                response.raise_for_status()
        except Exception as e:
            print(f"上传四级问题库失败: {e}")
            try:
                requests.delete(f"{update_url}?item_uuid=eq.{item_uuid}", headers=self.headers)
                response = requests.post(update_url, headers=update_headers, data=json.dumps(light_data))
                if response.status_code == 201:
                    return True
            except Exception as e2:
                print(f"删除并插入失败: {e2}")
            return False
    
    def sync_four_level_question_to_cloud(self, four_level_question_data):
        """同步四级问题库数据到云端"""
        print(f"开始同步四级问题库数据，数量: {len(four_level_question_data)}")
        cloud_data = self.get_four_level_question_from_cloud()
        cloud_dict = {item['item_uuid']: item for item in cloud_data}
        
        synced_count = 0
        for item in four_level_question_data:
            try:
                item_uuid, question_category, common_question, problem_description, specific_performance, measure_example, create_time, update_time, is_deleted = item
                data = {
                    'item_uuid': item_uuid,
                    'question_category': question_category,
                    'common_question': common_question,
                    'problem_description': problem_description,
                    'specific_performance': specific_performance,
                    'measure_example': measure_example,
                    'create_time': create_time or datetime.now().isoformat(),
                    'update_time': update_time,
                    'is_deleted': bool(is_deleted)
                }
                
                if item_uuid in cloud_dict:
                    cloud_item = cloud_dict[item_uuid]
                    try:
                        cloud_update_time = int(cloud_item.get('update_time', 0))
                        if update_time > cloud_update_time:
                            if self.upsert_four_level_question_to_cloud(data):
                                synced_count += 1
                    except:
                        if self.upsert_four_level_question_to_cloud(data):
                            synced_count += 1
                else:
                    if self.upsert_four_level_question_to_cloud(data):
                        synced_count += 1
            except Exception as e:
                print(f"同步四级问题库数据失败: {e}")
        
        print(f"四级问题库数据同步完成，同步数量: {synced_count}")
        return synced_count
    
    def sync_four_level_question_from_cloud(self, db):
        """从云端同步四级问题库到本地"""
        cloud_data = self.get_four_level_question_from_cloud()
        print(f"开始从云端同步四级问题库，数量: {len(cloud_data)}")
        local_data = db.get_all_four_level_question_for_sync()
        local_dict = {item[0]: item for item in local_data}
        
        synced_count = 0
        for cloud_item in cloud_data:
            item_uuid = cloud_item['item_uuid']
            try:
                if item_uuid in local_dict:
                    local_item = local_dict[item_uuid]
                    try:
                        cloud_update_time = int(cloud_item.get('update_time', 0))
                        local_update_time = int(local_item[7])
                        if cloud_update_time > local_update_time:
                            db.update_four_level_question_from_sync(cloud_item)
                            synced_count += 1
                    except:
                        db.update_four_level_question_from_sync(cloud_item)
                        synced_count += 1
                # 本地不存在的记录，不添加到本地，以本地数据为主
            except Exception as e:
                print(f"同步四级问题库失败: {e}")
        
        print(f"从云端同步四级问题库完成，同步数量: {synced_count}")
        return synced_count
    
    # ========== 配置数据同步 ==========
    def sync_config_to_cloud(self, config_data):
        """同步配置数据到云端"""
        print("开始同步配置数据")
        category_mapping, description_mapping = config_data
        synced_count = 0
        
        # 为配置数据生成唯一ID
        import hashlib
        
        # 同步问题类别
        for category_name, questions in category_mapping.items():
            try:
                # 生成类别ID
                category_id = int(hashlib.md5(category_name.encode()).hexdigest(), 16) % 1000000
                # 先同步类别
                category_data = {
                    'id': category_id,
                    'name': category_name,
                    'create_time': datetime.now().isoformat(),
                    'update_time': datetime.now().isoformat()
                }
                if self.upsert_question_category(category_data):
                    synced_count += 1
                    print(f"同步问题类别成功: {category_name}")
                
                # 再同步该类别的常见问题
                for question_name in questions:
                    # 生成问题ID
                    question_id = int(hashlib.md5((category_name + question_name).encode()).hexdigest(), 16) % 1000000
                    question_data = {
                        'id': question_id,
                        'category_name': category_name,
                        'name': question_name,
                        'create_time': datetime.now().isoformat(),
                        'update_time': datetime.now().isoformat()
                    }
                    if self.upsert_common_question(question_data):
                        synced_count += 1
                        print(f"同步常见问题成功: {question_name}")
                    
                    # 同步问题描述
                    if question_name in description_mapping:
                        # 生成描述ID
                        description_id = int(hashlib.md5(question_name.encode()).hexdigest(), 16) % 1000000
                        description = description_mapping[question_name]
                        description_data = {
                            'id': description_id,
                            'question_name': question_name,
                            'description': description,
                            'create_time': datetime.now().isoformat(),
                            'update_time': datetime.now().isoformat()
                        }
                        if self.upsert_problem_description(description_data):
                            synced_count += 1
                            print(f"同步问题描述成功: {question_name}")
            except Exception as e:
                print(f"同步配置数据失败: {e}")
                import traceback
                traceback.print_exc()
        
        print(f"配置数据同步完成，同步数量: {synced_count}")
        return synced_count
    
    def upsert_question_category(self, data):
        """上传问题类别数据到云端"""
        url = f"{self.supabase_url}/rest/v1/question_categories"
        headers = {**self.headers, 'Prefer': 'return=representation'}
        
        try:
            # 尝试更新
            print(f"尝试更新问题类别数据: 名称={data['name']}")
            response = requests.patch(
                f"{url}?name=eq.{data['name']}",
                headers=headers,
                data=json.dumps(data)
            )
            
            print(f"更新响应状态码: {response.status_code}")
            print(f"更新响应内容: {response.text}")
            
            if response.status_code == 200:
                # 检查响应内容是否为空，如果为空，说明没有找到记录，需要插入
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    return True
                else:
                    # 响应为空，尝试插入
                    print(f"更新响应为空，尝试插入: 名称={data['name']}")
                    response = requests.post(
                        url,
                        headers=headers,
                        data=json.dumps(data)
                    )
                    print(f"插入响应状态码: {response.status_code}")
                    print(f"插入响应内容: {response.text}")
                    return response.status_code == 201
            elif response.status_code == 404:
                # 尝试插入
                print(f"记录不存在，尝试插入: 名称={data['name']}")
                response = requests.post(
                    url,
                    headers=headers,
                    data=json.dumps(data)
                )
                print(f"插入响应状态码: {response.status_code}")
                print(f"插入响应内容: {response.text}")
                return response.status_code == 201
            else:
                return False
        except Exception as e:
            print(f"上传问题类别数据失败: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def upsert_common_question(self, data):
        """上传常见问题数据到云端"""
        url = f"{self.supabase_url}/rest/v1/common_questions"
        headers = {**self.headers, 'Prefer': 'return=representation'}
        
        try:
            # 尝试更新
            print(f"尝试更新常见问题数据: 类别={data['category_name']}, 问题={data['name']}")
            response = requests.patch(
                f"{url}?name=eq.{data['name']}&category_name=eq.{data['category_name']}",
                headers=headers,
                data=json.dumps(data)
            )
            
            print(f"更新响应状态码: {response.status_code}")
            print(f"更新响应内容: {response.text}")
            
            if response.status_code == 200:
                # 检查响应内容是否为空，如果为空，说明没有找到记录，需要插入
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    return True
                else:
                    # 响应为空，尝试插入
                    print(f"更新响应为空，尝试插入: 类别={data['category_name']}, 问题={data['name']}")
                    response = requests.post(
                        url,
                        headers=headers,
                        data=json.dumps(data)
                    )
                    print(f"插入响应状态码: {response.status_code}")
                    print(f"插入响应内容: {response.text}")
                    return response.status_code == 201
            elif response.status_code == 404:
                # 尝试插入
                print(f"记录不存在，尝试插入: 类别={data['category_name']}, 问题={data['name']}")
                response = requests.post(
                    url,
                    headers=headers,
                    data=json.dumps(data)
                )
                print(f"插入响应状态码: {response.status_code}")
                print(f"插入响应内容: {response.text}")
                return response.status_code == 201
            else:
                return False
        except Exception as e:
            print(f"上传常见问题数据失败: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def upsert_problem_description(self, data):
        """上传问题描述数据到云端"""
        url = f"{self.supabase_url}/rest/v1/problem_descriptions"
        headers = {**self.headers, 'Prefer': 'return=representation'}
        
        try:
            # 尝试更新
            print(f"尝试更新问题描述数据: 问题={data['question_name']}")
            response = requests.patch(
                f"{url}?question_name=eq.{data['question_name']}",
                headers=headers,
                data=json.dumps(data)
            )
            
            print(f"更新响应状态码: {response.status_code}")
            print(f"更新响应内容: {response.text}")
            
            if response.status_code == 200:
                # 检查响应内容是否为空，如果为空，说明没有找到记录，需要插入
                response_data = response.json()
                if isinstance(response_data, list) and len(response_data) > 0:
                    return True
                else:
                    # 响应为空，尝试插入
                    print(f"更新响应为空，尝试插入: 问题={data['question_name']}")
                    response = requests.post(
                        url,
                        headers=headers,
                        data=json.dumps(data)
                    )
                    print(f"插入响应状态码: {response.status_code}")
                    print(f"插入响应内容: {response.text}")
                    return response.status_code == 201
            elif response.status_code == 404:
                # 尝试插入
                print(f"记录不存在，尝试插入: 问题={data['question_name']}")
                response = requests.post(
                    url,
                    headers=headers,
                    data=json.dumps(data)
                )
                print(f"插入响应状态码: {response.status_code}")
                print(f"插入响应内容: {response.text}")
                return response.status_code == 201
            else:
                return False
        except Exception as e:
            print(f"上传问题描述数据失败: {e}")
            import traceback
            traceback.print_exc()
            return False
