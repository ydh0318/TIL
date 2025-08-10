import sys
from collections import deque

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1,T+1):
    # N 화덕의 크기, M 피자 개수
    N, M = map(int, input().split())
    pizza = deque(map(int, input().split()))
    oven = deque()
    
    # 피자를 넣고 돌릴 때 마다 확인하며 치즈의 양을 줄인다.
    # 초기화
    idx = 1
    for _ in range(N):
        oven.append((pizza.popleft(), idx))
        idx += 1
        
    last_pizza = -1
    
    while True:
        # 오븐에 피자가 존재하면
        if oven:
            cheese, number = oven.popleft()
        else: break
            
        # 화덕 돌리기
        # 피자 다 구워지면
        if cheese // 2 == 0:
            last_pizza = number
            # 넣을 피자 존재하면
            if pizza:
                oven.append((pizza.popleft(), idx))
                idx += 1
        else:
            # 다시 넣기
            oven.append((cheese//2, number))
        
    print(f'#{test_case} {last_pizza}')