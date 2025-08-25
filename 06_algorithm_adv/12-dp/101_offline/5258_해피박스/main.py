import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

def happy_box(N):
    '''
        N = 박스의 크기
        박스의 담긴 아이템의 크기의 합이 1부터 N까지의 최적합을 상향식으로 저장
    '''
    # dp[i][j]: i번째 아이템까지 고려했을 때, 크기 j의 박스에 담을 수 있는 최대 가치
    # 아이템 개수 M+1, 박스 크기 N+1 만큼의 배열 생성
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    # 첫번째 아이템 부터 M번째 아이템 까지 순회
    for i in range(1, M+1):
        item_size, item_price = items[i-1]  # 현재 아이템의 크기와 가격
        
        # 박스 크기를 1부터 N까지 순회
        for j in range(1, N + 1):
            # 현재 아이템의 크기가 박스 크기 j보다 클 경우
            if item_size > j: # 아이템을 넣을 수 없기 때문에 이전 템까지 고려한 최댓값 넣음
                dp[i][j] = dp[i-1][j]
            # 현재 아이템을 담을 수 있는 경우
            else: # 담을 때 최댄지 안담을 때 최댄지 고려
                # 담을 수 있는 공간 확보 후 그 당시에 최댓값 + 현재 최댓값
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_size] + item_price)
    return dp[M][N]
        

for tc in range(1,T+1):

    # 박스의 크기 N, 상품의 개수 M
    N, M = map(int, input().split())

    # i번째 행의 크기 Si와 가격 Pi
    items = [list(map(int, input().split())) for _ in range(M)]
    
    print(f'#{tc} {happy_box(N)}')
