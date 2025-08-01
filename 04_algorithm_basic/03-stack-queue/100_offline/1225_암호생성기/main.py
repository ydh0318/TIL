import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def code_creator(code : deque): # input : deque
    minus = 1
    while True:
        # 한 사이클 돌면 1로 초기화
        if minus == 6: minus = 1
        # 종료 조건
        if code[0] - minus < 0:
            code.popleft()
            code.append(0)
            break
        else:
            tmp = code.popleft() - minus
            code.append(tmp)
            minus += 1

    return code


for test_case in range(1,11):
    
    t = input()
    # deque로 암호 배열 생성
    code = deque(map(int, input().strip().split()))
    
    # 암호 생성 함수
    code = code_creator(code)

    # 문자열 변환
    code = list(map(str, code))
    code = ' '.join(code)
    print(f'#{test_case} {code}')