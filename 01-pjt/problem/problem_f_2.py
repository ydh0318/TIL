import csv
from collections import defaultdict

# 배우 출연 영화 집계 딕셔너리
actor_dict = defaultdict(int)

# 배우가 어떤 영화에 출연했는지를 기록하는 집합
actor_movies = defaultdict(set)

# CSV 파일 열기
with open('01-pjt\movie_cast.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        actor = row['name']
        movie_id = row['movie_id']
        
        # 해당 배우가 이 영화에 이미 기록되었는지 확인
        if movie_id not in actor_movies[actor]:
            actor_dict[actor] += 1
            actor_movies[actor].add(movie_id)

# 2편 이상 출연한 배우만 필터링
frequent_actors = {actor: count for actor, count in actor_dict.items() if count >= 2}

# 출력
print("2편 이상 출연한 배우 목록:")
for actor, count in frequent_actors.items():
    print(f"{actor}: {count}편")
    