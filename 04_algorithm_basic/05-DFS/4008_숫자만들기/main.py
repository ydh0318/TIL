import sys

sys.stdin = open('sample_input.txt', 'r')

def dfs(depth, current_total):
    global max_val, min_val
    # 종료 조건
    if depth == N:
         # 최대, 최소 업데이트
        if current_total > max_val: max_val = current_total
        if current_total < min_val: min_val = current_total
        return
    # op_counts의 숫자가 남아있으면 시도.
    for i in range(4):
        # 새로운 값에 할당 아니면 for문 돌때 같은 레벨의 값이 바뀌어 버림
        next = 0
        if op_counts[i] > 0: 
            # 연산자 사용
            op_counts[i] -= 1
            if i == 0 : next = current_total + numbers[depth]
            elif i == 1 : next = current_total - numbers[depth]
            elif i == 2 : next = current_total * numbers[depth]
            elif i == 3 : next = current_total // numbers[depth]
            dfs(depth+1, next)
            # backtracking
            op_counts[i] += 1
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 숫자의 개수
    # op_counts: [+,-,*,/] 연산자의 개수
    op_counts = list(map(int, input().split()))
    numbers = list(map(int, input().split()))  # 수식에 사용될 숫자
 
    # 최댓값과 최솟값 초기화
    max_val = -100000000
    min_val = 100000000
 
    dfs(1, numbers[0])
 
    result = max_val - min_val
    print(f"#{tc} {result}")