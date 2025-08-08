import sys
from collections import deque

sys.stdin = open('input.txt','r')

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 16 x 16의 미로에서 길은 0, 벽은 1로 표시된다.
# 미로의 시작점은 1,1이로 도착점은 13,13이다
# 출발점으로부터 도착점까지 갈 수 있는 길이 있는지 판단하는 프로그램 작성
def can_i_escape(row, col):
    queue.append((row,col))
    visited.add((row,col))
    while queue:
        row, col = queue.popleft()
        # 네 방향으로 탐색
        for k in range(4):
            ny = row + dy[k]
            nx = col + dx[k]
            # 범위 설정
            if nx < 0 or nx >= 100 or ny <0 or ny >= 100: continue
            # 이미 방문 한 경우
            if (ny, nx) in visited: continue
            # 길이 아닌 겨웅
            if maze[ny][nx] == 1: continue
            # 도착 지점인 경우
            if maze[ny][nx] == 3: return 1

            # 모든 조건들을 통과하면 queue에 넣고 탐색 진행
            visited.add((ny, nx))
            queue.append((ny,nx))
    return 0


for tc in range(1,11):
    t = input()
    maze = [list(map(int, input())) for _ in range(100)]
    # print(maze)
    # 방문 여부
    visited = set()
    # 후보군을 저장
    queue = deque()

    result = can_i_escape(1,1)
    print(f'#{tc} {result}')