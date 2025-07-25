# D. 영화 배우 정보 테이블 생성 및 데이터 수집과 전처리 
# 영화에 출연한 배우와 배역 정보를 수집합니다. 비중 있는 역할을 
# 파악하기 위해 출연 순서가 10 이하인 배우들만 선택하며 , 데이터에 
# 포함된 불필요한 줄바꿈 문자를 공백으로 변경하는 등의 데이터 정제 
# 작업을 수행합니다. 처리된 정보는 movie_cast.csv 파일로 저장합니다. 
# ⚫ 요구사항 번호: F04 
# ⚫ 구현: `problem_d.py` 파일을 수정하여 구현합니다. 
# ⚫ 필요한 정보: 배우 ID(cast_id), 영화 ID(movie_id), 배우 이름(name), 
# 배역 이름(character), 출연 순서(order).

import csv
import requests
from pprint import pprint

# TMDB API 키 설정
API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

# 문제 a에서 생성된 movies.csv 파일을 기반으로 영화 ID 목록 가져오기
with open('movies.csv','r', newline='',encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    print(csv_reader.fieldnames)
    csv_reader.fieldnames = [name.replace('\ufeff', '') for name in csv_reader.fieldnames]  # BOM 문자 제거
    print(csv_reader.fieldnames)

    movie_ids = [row['id'] for row in csv_reader]
    print(movie_ids)

# API 호출 함수
# movie_ids를 순회하며 배우 정보를 얻어옴
movies_cast_data = []  # 모든 배우 정보를 담을 리스트
fieldnames = ['cast_id', 'movie_id', 'name', 'character', 'order']
for movie_id in movie_ids:
    url = f"{BASE_URL}/movie/{movie_id}/credits?language=en-US"
    
    headers = {
        "accept": "application/json",
        "Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMTk1ZDMyZDU5MWYzZmI2MjMyZTZmZjk3YWUzMWY3NCIsIm5iZiI6MTc1MzQxMDAzMS42NDUsInN1YiI6IjY4ODJlOWVmOTY3NzI3NmM1MTE2YjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.C6aUUkV-TttIgOFBLZhzQZfiIwULakrimsvDVXG7d0o"
    }
    response = requests.get(url, headers=headers).json()
    # 배우 데이터 처리 함수
    # 요청이 성공했는지 확인 (상태 코드 200 = 성공)
    if response.get('cast'):
        for cast in response['cast']:
            if cast.get('order', 0) <= 10:
                movies_cast_data.append({
                    'cast_id': cast.get('cast_id'),
                    'movie_id': movie_id,
                    'name': cast.get('name'),
                    'character': cast.get('character').replace('\n', ' '),  # 줄바꿈 문자를 공백으로 변경
                    'order': cast.get('order')
                })
pprint(movies_cast_data)

# 데이터 수집 및 CSV 파일로 저장
with open('movie_cast.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(movies_cast_data)
print("\n✅ 'movie_cast.csv' 파일 저장이 완료되었습니다.")