def fibonacci_for_loop(n):
    # 기본 룰은 동일하게 적용해야 한다.
    # n이 0이면 0을 반환
    if n == 0:
        return 0
    # n이 1이면 1을 반환
    elif n == 1:
        return 1
    else:   # n이 2이상인 경우
        # 내 이전의 두항의 값이 무엇인지 알 수 있어야 함.
        first, second = 0, 1
        for _ in range(2, n+1):
            # 다음 피보나치 수는 이전 두 항의 함을 사용함.
            next_fib = first + second
            first = second
            second = next_fib
        return second

# 사용 예시
print(fibonacci_for_loop(10)) # 55
