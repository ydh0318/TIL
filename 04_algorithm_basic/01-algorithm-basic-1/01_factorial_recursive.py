def fact(n):
    '''
    재귀함수는 기본적으로 2가지 영역으로 구분지을 수 있음
    1. basic rule : 1이 되었을때는 1을 반환해야 한다.
    2. inductive rule : (n-1)로 자기 자신을 호출
    '''

    if n > 1:
        return n * fact(n-1) # 표현식 -> 하나의 값으로 평가
    else:
        return 1

# 사용 예시
print(fact(5))  # 5*4*3*2*1을 계산하여 120을 출력합니다

