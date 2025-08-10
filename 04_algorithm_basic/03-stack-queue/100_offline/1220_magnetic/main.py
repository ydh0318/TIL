import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

# n,s극이 붙어있는것을 하나의 교착상태로 본다
# 만약 각각 두개의 n,s극이 번갈아가며 있으면 두개로 본다.
# 1. 맨 위에 2이면 out.
# 2. 맨 아래에 1이면 out.
# 3. s극과 n극이 처음 만나면 교착상태.
#   3-1.
# 1이 N극, 2가 S극

for test_case in range(1,11):
    length = int(input())
    table = [list(map(int, input().split())) for _ in range(length)]
    total = 0
    stack = []
    
    for line in zip(*table):
        line = deque([x for x in line if x > 0])
        # print(line)
        stack.clear()
        deadlock = 0
        while line:
            
            top = line.popleft()
            # 1. S(2) 팝
            # 2. N(1) 다음에 오는 S들은 같은 교착상태
            # 3. 새로운 N이면
            #  3-1. 전부 N 이면 무시
            #  3-2. S면 2번 반복
            
            # 스택이 비어있을 때
            if len(stack) == 0:
                # S극이면 pop
                if top == 2: continue
                # N극이면 stack에 넣음
                else: stack.append(top)
            else: # 스택이 비어있지 않으면, 이미 N극이 존재한다는 뜻
                # N극이면
                if top == 1: stack.append(top)
                # S극이면
                else:
                    stack.clear()
                    deadlock += 1
        total += deadlock
        
        # print(deadlock)           
    print(f'#{test_case} {total}')    
    