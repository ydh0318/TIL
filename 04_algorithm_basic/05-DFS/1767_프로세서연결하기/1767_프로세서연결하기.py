import sys
sys.stdin = open('sample_input.txt')

dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 연결 할 코어 인덱스, 연결된 총 코어 수, 현재 연결된 전선의 길이
def dfs(core_idx, count_connected_core, current_line_length):
    global max_core_count
    global min_line_length
    # 종료조건
    if core_idx == len(core_list): # 모든 코어의 연결을 결정 했다면
        # 최대,최소 업데이트
        if count_connected_core > max_core_count:
            max_core_count = count_connected_core
            min_line_length = current_line_length
        # 2. 연결된 코어 수가 같다면, 전선 길이가 더 짧을 때만 업데이트
        elif count_connected_core == max_core_count:
            if current_line_length < min_line_length:
                min_line_length = current_line_length
        return
        
    # 가지치기 : 남은 코어를 모두 연결해도 맥스값보다 작다면 필요가 없음
    if max_core_count > count_connected_core + (len(core_list) - core_idx):
        return
    
    # --- 재귀 수행 ---

    # 경우 1: 현재 코어를 연결하지 않고 다음 코어로 넘어감
    dfs(core_idx + 1, count_connected_core, current_line_length)

    # 경우 2: 현재 코어를 4방향으로 연결 시도
    row, col = core_list[core_idx]
    
    # 상, 하, 좌, 우 4방향 탐색
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상, 하, 좌, 우
        
        path = [] # 연결할 전선의 경로를 저장할 리스트
        is_connectable = True
        
        # 현재 위치에서부터 경계까지 한 칸씩 이동하며 확인
        nr, nc = row + dr, col + dc
        while 0 <= nr < N and 0 <= nc < N:
            if mxynos[nr][nc] != 0: # 다른 코어나 전선이 있다면
                is_connectable = False
                break
            path.append((nr, nc))
            nr += dr
            nc += dc
            
        # 전선 연결이 가능하다면
        if is_connectable:
            # 1. 전선 설치 (2로 표시)
            for r, c in path:
                mxynos[r][c] = 2
            
            # 2. 다음 코어로 재귀 호출
            dfs(core_idx + 1, count_connected_core + 1, current_line_length + len(path))
            
            # 3. 전선 제거 (백트래킹)
            for r, c in path:
                mxynos[r][c] = 0
        
        
T = int(input())

for tc in range(1, T+1):

    # N x N크기의 멕시노스
    N = int(input())
    max_core_count = 0
    min_line_length = float('inf')
    
    mxynos = [list(map(int, input().split())) for _ in range(N)]
    core_list = []
    for r in range(N):
        for c in range(N):
            # 가장자리가 아닌 코어만 리스트에 추가
            if r > 0 and r < N - 1 and c > 0 and c < N - 1 and mxynos[r][c] == 1:
                core_list.append((r, c))
                
    dfs(0,0,0)
    print(f'#{tc} {min_line_length}')