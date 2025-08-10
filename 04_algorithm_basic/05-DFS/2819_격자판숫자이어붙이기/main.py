import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(depth, current_number, row, col):
    # 격자판 범위 설정
    # if (col < 0 and col > 3) or (row < 0 and row > 3):
    #     return
    # 종료 조건
    if depth == 7:
        # 7자리 숫자 만들어지면 numbers 집합에 추가
        numbers.add(current_number)
        return
    # 상하좌우로 움직여야 함.
    for x, y in position:
        if 0 <= row + y <= 3 and 0 <= col + x <= 3:
            # 새로운 리스트에 값 추가해서 넘겨줌
            next_number = current_number + str(grid[row+y][col+x])
            dfs(depth+1, next_number, row + y , col + x)
 
T = int(input())
for tc in range(1, T + 1):
    # 격자
    grid = [list(map(int, input().split())) for _ in range(4)]
 
    position = [(1,0), (-1,0), (0,1), (0,-1)]
    # 최종 숫자 집합
    numbers = set()
    # 생성 숫자 담을 리스트
    result = ''
    for i in range(4):
        for j in range(4):
            # result += str(grid[i][j])
            dfs(1, str(grid[i][j]), i, j)
 
    print(f"#{tc} {len(numbers)}")