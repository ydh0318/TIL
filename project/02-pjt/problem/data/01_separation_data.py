import os
import django
import csv
import sys
from datetime import datetime

# --------------------------------------------------------------------------
# [중요] Django 환경 설정
# --------------------------------------------------------------------------
# 이 스크립트가 프로젝트의 위치를 찾을 수 있도록 경로를 설정합니다.
# 현재 파일의 위치를 기준으로 프로젝트 루트 디렉토리를 계산합니다.
# (예: C:\Users\...\problem\data -> C:\Users\...\problem)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 이제 Django 설정을 로드할 수 있습니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pjt_02.settings')
django.setup()
# --------------------------------------------------------------------------

# Django 환경이 설정된 후에 모델을 임포트해야 합니다.
from movies.models import Movie, Genre, Cast, Review

# CSV 파일 경로 설정 (이 스크립트 파일과 동일한 위치에 있다고 가정)
MOVIES_CSV_PATH = 'movies.csv'
DETAILS_CSV_PATH = 'movie_details.csv'
CAST_CSV_PATH = 'movie_cast.csv'
REVIEWS_CSV_PATH = 'movie_reviews.csv'

def import_data_from_csv():
    """
    모든 CSV 파일을 읽고 Django 데이터베이스에 데이터를 삽입하는 메인 로직.
    """
    
    # 1. 영화 기본 정보 및 상세 정보 로드
    print("Importing movies and genres...")
    details_data = {}
    with open(DETAILS_CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            details_data[row['movie_id']] = row

    with open(MOVIES_CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_id = row['id']
            
            if movie_id not in details_data:
                continue

            detail_row = details_data[movie_id]
            
            try:
                release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
            except (ValueError, TypeError):
                release_date = None

            movie = Movie.objects.create(
                id=movie_id,
                title=row['title'],
                release_date=release_date,
                popularity=float(row['popularity']),
                budget=int(detail_row['budget']),
                revenue=int(detail_row['revenue']),
                runtime=int(detail_row['runtime'])
            )

            genre_names = detail_row['genres'].split(', ')
            for genre_name in genre_names:
                if genre_name:
                    genre, _ = Genre.objects.get_or_create(genre=genre_name)
                    movie.genres.add(genre)
    print(f"{Movie.objects.count()} movies imported.")

    # 2. 출연진 정보 로드
    print("Importing cast...")
    with open(CAST_CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                movie = Movie.objects.get(id=int(row['movie_id']))
                Cast.objects.create(
                    movie=movie,
                    name=row['name'],
                    character=row['character'],
                    order=int(row['order'])
                )
            except Movie.DoesNotExist:
                continue
    print(f"{Cast.objects.count()} cast members imported.")

    # 3. 리뷰 정보 로드
    print("Importing reviews...")
    with open(REVIEWS_CSV_PATH, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                movie = Movie.objects.get(id=int(row['movie_id']))
                Review.objects.create(
                    movie=movie,
                    author=row['author'],
                    content=row['content'],
                    rating=float(row['rating'])
                )
            except Movie.DoesNotExist:
                continue
    print(f"{Review.objects.count()} reviews imported.")


def main():
    """
    스크립트의 시작점 (main 함수 역할)
    """
    print('Starting database seeding...')

    # 기존 데이터 초기화
    print('Deleting existing data...')
    Cast.objects.all().delete()
    Review.objects.all().delete()
    Movie.objects.all().delete()
    Genre.objects.all().delete()
    
    # CSV 데이터 임포트 함수 호출
    import_data_from_csv()
    
    print('Database seeding completed successfully!')


# 이 파일이 직접 실행될 때 main() 함수를 호출합니다.
if __name__ == '__main__':
    main()
