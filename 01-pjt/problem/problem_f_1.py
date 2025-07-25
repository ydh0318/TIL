import csv
import requests

# ⬇️ 실제 본인의 API 키를 입력하세요.
API_KEY = '0195d32d591f3fb6232e6ff97ae31f74'
BASE_URL = 'https://api.themoviedb.org/3'

def get_movie_title(movie_id):
    """
    영화 ID를 받아 TMDB API에서 영화 제목을 가져오는 함수
    """
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': API_KEY,
        'language': 'en-US' # 한글 제목을 우선으로 가져옴
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # 한글 제목이 없으면 영문 제목을 가져옴
            return data.get('title') or data.get('original_title')
    except requests.exceptions.RequestException as e:
        print(f"API 요청 오류: {e}")
    
    return "제목을 찾을 수 없음"

max_profit=0
movie_profits = []

file_path='movie_details.csv'
with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        budget = int(row['budget'])
        revenue = int(row['revenue'])

        if budget and revenue:
            profit=((revenue-budget)/budget)*100
            movie_profits.append([profit, row['movie_id']])
            # profit=((revenue-budget)/budget)*100
            # print(profit, row['movie_id'])

            # if profit == max(profit,max_profit):
            #     movie=row['movie_id']

movie_profits.sort()
top_movie_id = movie_profits[-1][1]
top_movie_title = get_movie_title(top_movie_id)
print(top_movie_title)