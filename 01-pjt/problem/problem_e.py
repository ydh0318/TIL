import requests
import csv
import json

# --- 설정 부분 ---
API_KEY = '0195d32d591f3fb6232e6ff97ae31f74'
BASE_URL = 'https://api.themoviedb.org/3'

# 입출력 파일 경로
REVIEWS_CSV_PATH = 'movie_reviews_1.csv'
RATINGS_CSV_PATH = 'movie_ratings.csv'


def get_movie_details_from_api(movie_id):
    """TMDB API에서 영화의 상세 정보를 가져옵니다 (평균 평점, 투표 수)."""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {'api_key': API_KEY}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'average_rating': data.get('vote_average'),
            'vote_count': data.get('vote_count')
        }
    return None


def calculate_rating_distribution(reviews_csv_path):
    """movie_reviews_1.csv 파일을 읽어 각 영화의 평점 분포를 계산합니다."""
    distributions = {}
    
    with open(reviews_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie_id = row['movie_id']
            rating = int(float(row['rating']))

            # [수정됨] 해당 영화의 딕셔너리가 없으면 빈 딕셔너리로 생성
            if movie_id not in distributions:
                distributions[movie_id] = {}
            
            if 1 <= rating <= 10:
                # [수정됨] 현재 평점의 카운트를 가져와 1을 더함 (없으면 0에서 시작)
                current_count = distributions[movie_id].get(rating, 0)
                distributions[movie_id][rating] = current_count + 1
                    
    return distributions


# --- 메인 실행 로직 ---
print("리뷰 파일 분석 및 평점 분포 계산 중...")
rating_distributions = calculate_rating_distribution(REVIEWS_CSV_PATH)

all_movie_ratings = []
fieldnames = ['movie_id', 'average_rating', 'vote_count', 'rating_distribution']

for movie_id, dist_map in rating_distributions.items():
    print(f"영화 ID '{movie_id}'의 API 데이터 수집 중...")
    
    api_data = get_movie_details_from_api(movie_id)
    
    if api_data:
        # 평점 분포 딕셔너리를 JSON 문자열로 변환
        distribution_str = json.dumps(dist_map, sort_keys=True)
        
        final_data = {
            'movie_id': movie_id,
            'average_rating': api_data['average_rating'],
            'vote_count': api_data['vote_count'],
            'rating_distribution': distribution_str
        }
        all_movie_ratings.append(final_data)

with open(RATINGS_CSV_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_movie_ratings)

print(f"\n'{RATINGS_CSV_PATH}' 파일이 성공적으로 생성되었습니다. ✅")