import requests 
from pprint import pprint

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
#print(response)
# 유저정보
user_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
# print(user_response)

completed_todos = [] # 최종 결과물을 담을 리스트
fields = ['id', 'title']

pprint(response)
for item in response:
    # 전체 데이터 중, completed가 True인 경우에 대해서만 사용할 것
    # 임시 변수 item에 할당된 데이터 타입은 dict 따라서, completed에 대해서 물어보자면,
    # key가 completed인 경우, 그 value가 True인 경우만 출력
    # if item['completed'] == True:
    #     print(item)
    if item.get('completed'):
        # 그중, 내가 필요로 하는 2개의 필드 id, title만 따로 모은다.
        temp_item = {}
        for key in fields: # 'id', 'title'
            #temp_item['id'] = item['id'] value
            # ctrl + alt + 위아래 : 커서복사
            # ctrl + shitf + 좌우 : 단어 단위 이동
            temp_item[key] = item[key]
            for user in user_response:
                if user['id'] == item['userId']:
                    user_info = {
                        'id':user['id'] ,
                        'name':user['name'] ,
                        'username':user['username'] ,
                        'email':user['email']
                    }
                    temp_item['user'] = user_info
        completed_todos.append(temp_item)
    #pprint(completed_todos)