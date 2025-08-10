
import sys

sys.stdin = open('input.txt','r')


# 총 10개의 테스트 케이스를 순회
for tc in range(1, 11):
    
    # 테스트 케이스 번호
    t = int(input())
    
    # 100x100 크기의 사다리 정보 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 1. 도착점 '2'의 x좌표 찾기
    # ladder[99]는 가장 아래 행을 의미
    x = ladder[99].index(2)
    y = 99 # 시작 y좌표

    # 2. y가 0 (맨 위)에 도달할 때까지 루프 반복
    while y > 0:
        
        # 3. 좌/우 우선 탐색
        # 왼쪽 확인: 현재 위치가 가장 왼쪽이 아니고(x > 0), 왼쪽에 길이(1) 있다면
        if x > 0 and ladder[y][x - 1] == 1:
            # 왼쪽 길이 끝날 때까지 계속해서 왼쪽으로 이동
            while x > 0 and ladder[y][x - 1] == 1:
                x -= 1
                
        # 오른쪽 확인: 현재 위치가 가장 오른쪽이 아니고(x < 99), 오른쪽에 길이(1) 있다면
        elif x < 99 and ladder[y][x + 1] == 1:
            # 오른쪽 길이 끝날 때까지 계속해서 오른쪽으로 이동
            while x < 99 and ladder[y][x + 1] == 1:
                x += 1
        
        # 4. 좌/우 이동이 끝나면(또는 원래 없었으면) 위로 한 칸 이동
        # y는 매 루프마다 반드시 1씩 감소하여 무한 루프에 빠지지 않음
        y -= 1
            
    # 루프가 끝나면 y는 0이 되고, 이때의 x좌표가 최종 출발점
    print(f'#{tc} {x}')    
    t = int(input())
    
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착점
    endpoint = ladder[-1].index(2)
    # print(endpoint)
    y = len(ladder) - 1
    x = endpoint

    startpoint = 0
    while y > 0:
    # 좌/우 이동을 먼저 처리하기 위해 방문 표시 (선택 사항)
    # ladder[y][x] = 0 
        # 1. 왼쪽 확인: 경계 안에 있고 왼쪽에 길이 있다면
        if x > 0 and ladder[y][x-1] == 1:
            x -= 1 # 왼쪽으로 한 칸 이동
        # 2. 오른쪽 확인: 경계 안에 있고 오른쪽에 길이 있다면
        elif x < 99 and ladder[y][x+1] == 1:
            x += 1 # 오른쪽으로 한 칸 이동
        # 3. 좌우에 길이 없으면 위로 한 칸 이동
        else:
            y -= 1
            
    print(f'#{tc} {startpoint}')
    