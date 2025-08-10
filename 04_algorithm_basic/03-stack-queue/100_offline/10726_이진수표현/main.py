import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())

    # 1. 마지막 N 비트가 1인 비트마스크 생성
    # 15 - > 01111
    mask = (1 << N) - 1

    # 2. M과 마스크를 AND 연산한 결과가 마스크 자신과 같은지 확인
    if M & mask == mask: result = 'ON'
    else: result = 'OFF'

    print(f'#{i} {result}')