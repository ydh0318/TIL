# 사용자들의 평가를 분석하기 위해 각 영화에 달린 리뷰 데이터를 수집
# 합니다. 모든 리뷰를 수집하는 것이 아니라, 평점이 5점 이상인 리뷰만 
# 필터링해야 합니다. 또한, 리뷰 내용이 비어있는 경우 '내용 없음'으로 
# 처리하는 전처리 과정을 포함하며, 최종 결과를 movie_reviews.csv 파
# 일로 저장합니다. 
# ⚫ 요구사항 번호: F03 
# ⚫ 구현: `problem_c.py` 파일을 수정하여 구현합니다. 
# ⚫ 필요한 정보: 리뷰 ID(review_id), 영화 ID(movie_id), 작성자(author), 
# 리뷰 내용(content), 평점(rating).
import csv
from pprint import pprint

# TMDB API 키 설정
API_KEY = ''
BASE_URL = 'https://api.themoviedb.org/3'

# 영화 ID 리스트를 movies.csv 파일에서 읽어옴
movie_ids = []
with open('movies.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row['\ufeffid'])
        movie_ids.append(row['\ufeffid'])  # '\ufeff'는 BOM 문자로, CSV 파일에서 첫 번째 열의 이름에 포함될 수 있음
    print(movie_ids)

# API 호출 함수
import requests

url = "https://api.themoviedb.org/3/movie/1061474/reviews?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": ""
}

response = requests.get(url, headers=headers)

# 리뷰 데이터 처리 함수
fieldnames = ['review_id', 'movie_id', 'author', 'content', 'rating']

movies_reviews_data = []  # 모든 리뷰 정보를 담을 리스트
if response.status_code == 200:
    data = response.json()
    index = 0
    # 실제 리뷰 목록은 응답(data)의 'results' 키 안에 리스트 형태로 들어있습니다.
    for review in data['results']:
        if review.get('author_details', {}).get('rating', 0) >= 5:
            movies_reviews_data.append({
                'review_id': review.get('id'),
                'movie_id': movie_ids[index],
                'author': review.get('author'),
                'content': review.get('content') if review.get('content') else '내용 없음',
                'rating': review.get('author_details', {}).get('rating', 0)
            })
            index += 1
    print("데이터 처리 완료!")

for review in movies_reviews_data:
    print(review['review_id'], review['movie_id'], review['author'], review['rating'])

# 데이터 수집 및 CSV 파일로 저장

with open("movies_reviews.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(movies_reviews_data)
    print("CSV 파일로 저장 완료")