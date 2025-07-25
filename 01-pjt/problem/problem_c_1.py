import requests
import csv

# --- 설정 부분 ---
API_KEY = '0195d32d591f3fb6232e6ff97ae31f74'  # ⬅️ 실제 본인의 API 키를 이곳에 입력하세요.
BASE_URL = 'https://api.themoviedb.org/3'
PAGES_TO_FETCH = 20  # ⬅️ 수집할 페이지 수를 설정합니다.


# --- 1. movies.csv 파일에서 영화 ID 리스트 읽어오기 ---
movie_ids = []
try:
    with open('movies.csv', 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movie_ids.append(row['id'])
except FileNotFoundError:
    print("오류: 'movies.csv' 파일을 찾을 수 없습니다.")
    exit()


# --- 2. 데이터 수집 및 처리 ---
all_reviews_data = []  # 모든 영화의 리뷰를 담을 최종 리스트
fieldnames = ['review_id', 'movie_id', 'author', 'content', 'rating']

# 각 영화 ID에 대해 반복
for movie_id in movie_ids:
    print(f"=== 영화 ID '{movie_id}' 리뷰 수집 시작 ===")
    
    # 지정된 페이지 수만큼 반복
    for page in range(1, PAGES_TO_FETCH + 1):
        # API 요청 URL 및 파라미터 설정
        url = f"{BASE_URL}/movie/{movie_id}/reviews"
        params = {
            'api_key': API_KEY,
            'language': 'en-US',
            'page': page
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            reviews = data.get('results', [])

            # 해당 페이지에 더 이상 리뷰가 없으면 다음 영화로 넘어감
            if not reviews:
                print(f"페이지 {page}에 리뷰가 없어 다음 영화로 넘어갑니다.")
                break

            # 각 리뷰를 처리
            for review in reviews:
                rating = review.get('author_details', {}).get('rating')

                # 평점이 5점 이상인 리뷰만 필터링
                if rating is not None and rating >= 5:
                    content = review.get('content', '').strip()
                    
                    # 최종 데이터 리스트에 추가
                    all_reviews_data.append({
                        'review_id': review.get('id'),
                        'movie_id': movie_id,  # 현재 조회 중인 영화의 ID
                        'author': review.get('author'),
                        'content': content if content else '내용 없음',
                        'rating': rating
                    })
        else:
            print(f"오류: 영화 ID '{movie_id}', 페이지 {page} 요청 실패 (상태 코드: {response.status_code})")
            # 요청 실패 시 해당 영화의 다음 페이지 수집을 중단
            break

print("\n=== 모든 데이터 처리 완료! ===")


# --- 3. CSV 파일로 저장 ---
with open("movie_reviews_1.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_reviews_data)

print("CSV 파일 저장 완료: movie_reviews_1.csv")