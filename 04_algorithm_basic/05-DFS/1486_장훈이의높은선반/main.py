import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

def dfs(idx, current_tower):
    global max_tower
    # 종료조건 : 지금까지 만든 키가 B보다 높으면
    if current_tower >= B:
        # 큰것중 가장 작은것
        max_tower = min(max_tower, current_tower)
        return
    # 점원을 모두 사용했으면
    if idx == N: return
    # 재귀 idx번째 점원 사용하냐 안하냐
    dfs(idx + 1, current_tower + H[idx])
    dfs(idx + 1, current_tower)

for tc in range(1, T+1):
    # 점원의 수, 탑의 높이
    N, B = map(int, input().split())
    # 점원들의 키
    H = list(map(int, input().split()))
    
    max_tower = sum(H)
    dfs(0,0)
    print(f'#{tc} {max_tower - B}')