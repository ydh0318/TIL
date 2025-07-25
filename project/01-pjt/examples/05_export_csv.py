'''
    외부 라이브러리나 모듈등을 import 해와야 할 때,
    그 import가 필요할 때 마다 받아서 사용
'''
# 요청을 보내야 한다
import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
completed_todos = [] # 최종 결과물을 담을 리스트
fields = ['id', 'title']

for item in response:
    if item.get('completed'):
        temp_item = {}
        for key in fields: # 'id', 'title'    
            temp_item[key] = item[key]
        completed_todos.append(temp_item)

with open('completed_todos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fields)
    writer.writeheader()  # 헤더 작성
    writer.writerows(completed_todos) # 여러 행을 한 번에 작성
