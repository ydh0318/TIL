def fibonacci_memoization(n):
    # n이 2 이상이고, memo[n]번째가 아직 계산되지 않았으면 계산
    print(memo,n)
    if n >= 2 and memo[n] == 0:
        memo[n] = fibonacci_memoization(n-1) + fibonacci_memoization(n-2)
    return memo[n]

n = 10
# 10개의 값을 기록하는 list
memo = [0] * (n+1)  # 0부터 10까지 총 열한개
# basic rule
memo[1] = 1

fibonacci_memoization(10)
print(memo)