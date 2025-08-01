import sys

sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = input()    # 테스트 케이스 번호 입력
    answer = 0

    data = [list(map(int, input().split())) for _ in range(100)]
    # for _ in range(100):
    #     tmp_list = list(map(int, input().split()))
    #     data.append(tmp_list)

    # 행 계산
    for i in range(100):
        row_sum = sum(data[i])
        if row_sum > answer:
            answer = row_sum
    # 열 계산
    col_data = list(zip(*data))
    for i in range(100):
        col_sum = sum(col_data[i])
        if col_sum > answer:
            answer = col_sum
    # 대각1 계산
    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += data[i][i]
        if diagonal_sum > answer:
            answer = diagonal_sum
    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += data[99-i][i]
        if diagonal_sum > answer:
            answer = diagonal_sum
        

    print(f'#{tc} {answer}')