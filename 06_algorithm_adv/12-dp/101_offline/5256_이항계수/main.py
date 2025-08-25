import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):

    # n 전체항의 계수, a x의 계수, b y의 계수
    n, a, b = map(int, input().split())

    '''
        이항계수의 일반항
        nCk = n-1Ck-1 + n-1Ck
    '''

    # k가 1이거나 n이면 1

    # dp 테이블 
    def bino(n ,k):

        dp = [ [0 for _ in range(k+1)] for _ in range(n+1) ]

        for i in range(n+1):
            for j in range(min(i,k)+1):
                if j == 0 or i == j: dp[i][j] = 1
                else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp[n][k]
    
    print(f'#{tc} {bino(n,b)}')
