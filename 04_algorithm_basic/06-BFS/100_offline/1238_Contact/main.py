import sys
from collections import deque
from collections import defaultdict

sys.stdin = open('input.txt','r')

# 비상 연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때,
# 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성

# 인접리스트로 그래프 구현 한 후.
# 순서 인자를 넘기며 가장 늦게 연락을 받는 사람 중 번호가 가장 큰 사람을 구해야함.


def contact(start, depth): # start : 인접리스트 키 값, 전달받은 순서
    max_depth = 0
    last_level_people = []
    # 사람과 깊이를 저장
    queue.append((start, depth))
    # 사람만 저장
    visited.add(start)

    while queue:
        current_person, current_depth = queue.popleft()

        # 현재 깊이가 맥스 깊이보다 크면
        if current_depth > max_depth:
            max_depth = current_depth
            # 마지막에 연락 받는 사람들 초기화
            last_level_people = [current_person]
        # 현재 깊이 == 맥스 깊이면 리스트에 추가
        elif current_depth == max_depth:
            last_level_people.append(current_person)

        # 현재 사람에서 갈 수 있는 사람들이 후보
        for destination in adj_list.get(current_person,[]):
            # 방문하지 않았으면
            if destination not in visited:
                visited.add(destination)
                queue.append((destination,current_depth + 1))
        # 더 방문할 곳이 없으면, 늦게 받은 사람 중 번호가 가장 큰 사람 리턴
    return max(last_level_people)


for tc in range(1,11):
    # 데이터의 길이와 시작 점
    length, start = map(int, input().split())
    network = list(map(int, input().split()))
    adj_list = defaultdict(list)
    # 홀수 짝수 : from to 형식
    for i in range(0,length,2):
        # 출발지가 key, 도착지가 value
        adj_list[network[i]].append(network[i+1])
    # 방문 여부
    visited = set()
    # 후보군을 저장
    queue = deque()
    result = contact(start, 0)
    print(f'#{tc} {result}')