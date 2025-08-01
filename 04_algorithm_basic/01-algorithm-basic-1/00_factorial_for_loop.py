# 팩토리얼을 반복문으로 구현

# 구하고자 하는 값 N
N = 5
answer = 1  # 초기값 1로 초기화
for i in range(2, N+1):
    answer *= i

print(answer)
# 코드 실행은 crtl + shift + f10
