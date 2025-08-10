import sys
from collections import deque

sys.stdin = open('sample_input.txt', 'r')

def raser_cutting(stick):
    stack = []
    total = 0
    for i in range(len(stick)):
        # 여는 괄호면 삽입
        if stick[i] == '(':
            stack.append(stick[i])
        # 닫는 괄호면
        else:
            stack.pop()
            if stick[i-1] == '(': # 이전 괄호가 여는괄호면 레이저
                total += len(stack)
            else: # 막대기가 없어지며 조각이 하나 생김
                total += 1 
    return total



T = int(input())
sticks = [input() for _ in range(T)]
    
for i in range(1,T+1):
    print(f'#{i} {raser_cutting(sticks[i-1])}')