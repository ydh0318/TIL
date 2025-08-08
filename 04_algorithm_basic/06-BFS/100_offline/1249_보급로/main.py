import sys
sys.stdin = open('input.txt')

# 2차 세계 대전에서 연합군과 독일군의 전투가 점점 치열해지고 있다. 
# 출발지에서부터 도착지까지 가기 위한 도로 복구 작업을 수행해야 한다.
# 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오

# 지도 정보는 각 칸마다 파여진 도로의 깊이가 주어진다.
# 출발지와 도착지를 제외한 곳이 0인 곳은 복구 작업이 불필요한 곳이다.
from collections import deque

#     상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def get_repair_time(row, col):
    # 지도 정보를 통해 복구 시간을 계산한다.

    # queue 정의
    queue = deque((row,col))
    # 방문 위치 저장
    visited = set()
    visited.add((row,col))

    # 상하좌우로 움직이며 탐색한다.
    for i in range(4):
        ny = row + dy[i]
        nx = col + dx[i]
        # 종료 조건
        if ny == N-1 and nx == N-1:
            return
        # 가지치기 조건
        # 현재까지 저장한 수리시간보다 크면 가지 않는다.

T = int(input())

for tc in range(1, T + 1):
    # N x N 크기의 지도
    N = int(input())

    map = [list(input()) for _ in range(N)]
    
    get_repair_time(0,0)
    print(f'#{tc} ')