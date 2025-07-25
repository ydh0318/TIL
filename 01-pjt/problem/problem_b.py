'''
영화 상세 정보 테이블 생성 및 데이터 수집 
기본 정보만으로는 서비스에 활용하기 부족하므로, F01에서 수집한 
개별 영화 ID를 바탕으로 각 영화의 상세 정보를 추가로 수집합니다. 
영화의 예산, 수익, 총 상영 시간, 그리고 장르 정보를 추출하여 
movie_details.csv 파일로 저장합니다.. 
⚫ 요구사항 번호: F02 
⚫ 구현: `problem_b.py` 파일을 수정하여 구현합니다. 
⚫ 필요한 정보: 영화 ID(movie_id), 예산(budget), 수익(revenue), 상영 
시간(runtime), 장르(genres).
'''

import requests
import csv

# API 호출 함수
API_KEY = 'YOUR_API'
BASE_URL = 'https://api.themoviedb.org/3'

# 입출력 파일 경로
MOVIES_CSV_PATH = 'movies.csv'
DETAILS_CSV_PATH = 'movie_details.csv'

# 영화 상세 데이터 처리 함수
def get_movie_details(movie_id):
    """
    주어진 영화 ID를 사용하여 TMDB API에서 영화 상세 정보를 요청하고,
    필요한 데이터(예산, 수익, 상영 시간, 장르)를 추출하여 반환합니다.
    (모든 요청이 성공한다고 가정합니다)
    """
    # API 요청 URL 구성
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    
    # 응답을 JSON으로 변환
    data = response.json()

    # 'genres'는 딕셔너리 리스트이므로, 이름만 추출해 ','로 연결된 문자열로 만듭니다.
    genres_str = ', '.join([genre['name'] for genre in data.get('genres', [])])

    movie_detail = {
        'movie_id': data.get('id'),
        'budget': data.get('budget'),
        'revenue': data.get('revenue'),
        'runtime': data.get('runtime'),
        'genres': genres_str
    }
    return movie_detail

# CSV 파일에서 영화 ID 읽기
# 'movies.csv' 파일을 읽어 ID를 리스트에 저장합니다.
movie_ids = []
with open(MOVIES_CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_ids.append(row['\ufeffid'])
# CSV 파일의 헤더(필드명)를 정의합니다.
fieldnames = ['movie_id', 'budget', 'revenue', 'runtime', 'genres']

# 데이터 수집 및 CSV 파일로 저장
with open(DETAILS_CSV_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # CSV 파일에 헤더 작성
    writer.writeheader()

    # 각 영화 ID에 대해 상세 정보 수집 및 파일에 쓰기
    for movie_id in movie_ids:
        print(f"영화 ID '{movie_id}'의 상세 정보 수집 중...")
        details = get_movie_details(movie_id)
            
        # 상세 정보가 성공적으로 수집된 경우에만 파일에 기록
        if details:
            writer.writerow(details)

print(f"\n'{DETAILS_CSV_PATH}' 파일이 성공적으로 생성되었습니다. ✅")