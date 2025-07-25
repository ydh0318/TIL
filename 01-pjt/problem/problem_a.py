# A. 기본 영화 정보 테이블 생성 및 데이터 수집 
# 인기 있는 영화 목록을 API를 통해 조회하여, 모든 데이터 처리의 
# 기준이 될 기본 영화 정보를 수집합니다. 각 영화의 고유 ID, 제목, 
# 개봉일, 그리고 인기도 점수를 추출하여 movies.csv 파일로 저장해야 
# 합니다. 
# ⚫ 요구사항 번호: F01 
# ⚫ 구현: `problem_a.py` 파일을 수정하여 구현합니다. 
# ⚫ 필요한 정보: 영화 ID(id), 영화 제목(title), 개봉일(release_date), 
# 인기 점수(popularity)

# TMDB API 키 설정
API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

# API 호출 함수
import requests
from pprint import pprint
import csv

url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMTk1ZDMyZDU5MWYzZmI2MjMyZTZmZjk3YWUzMWY3NCIsIm5iZiI6MTc1MzQxMDAzMS42NDUsInN1YiI6IjY4ODJlOWVmOTY3NzI3NmM1MTE2YjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.C6aUUkV-TttIgOFBLZhzQZfiIwULakrimsvDVXG7d0o"
}

response = requests.get(url, headers=headers)
# print(response .items())

# 영화 데이터 처리 함수
movies_data = [] # 모든 영화 정보를 담을 리스트
# 요청이 성공했는지 확인 (상태 코드 200 = 성공)
if response.status_code == 200:
    data = response.json()
    
    # 실제 영화 목록은 응답(data)의 'results' 키 안에 리스트 형태로 들어있습니다.
    for movie in data['results']:
        movies_data.append({
            'id': movie.get('id'),
            'title': movie.get('title'),
            'release_date': movie.get('release_date'),
            'popularity': movie.get('popularity')
        })
    print("데이터 처리 완료!")
    pprint(movies_data)
else:
    # API 키가 잘못되었거나 다른 문제가 있을 경우 에러 메시지를 출력합니다.
    print(f"API 에러 발생: {response.status_code}")
    pprint(response.json()) # 에러 내용 확인


# 데이터 수집 및 CSV 파일로 저장

if movies_data:
    with open('movies.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['id', 'title', 'release_date', 'popularity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(movies_data)
    
    print("\n✅ 'movies.csv' 파일 저장이 완료되었습니다.")
else:
    print("\n수집된 데이터가 없어 파일을 저장하지 않았습니다.")
