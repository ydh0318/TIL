# 코드 변환
code_dict = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

def decode(code):
    decoded = ''
    for i in range(0, len(code), 7):
        chunk = ''.join(map(str, code[i:i+7]))
        if chunk not in code_dict:
            return None
        decoded += code_dict[chunk]
    return decoded

# 암호코드 판별 함수
def is_valid(code):

    # 코드길이 56 판별
    if len(code) != 56:
        return 0

    decoded  = decode(code)
    if decoded is None:
        return 0

    odd_sum = sum(int(decoded[i]) for i in range(0, 8, 2))
    even_sum = sum(int(decoded[i]) for i in range(1, 8, 2))

    total = odd_sum * 3 + even_sum
    return odd_sum + even_sum if total % 10 == 0 else 0

T = int(input())
for test_case in range(1,T+1):
    N ,M = map(int, input().split())


    encoded = [list(map(int, input().strip())) for _ in range(N)]
    # 1. 코드가 적힌 줄을 찾는다.
    for line in encoded:
        if 1 in line:
            # 암호는 1로 끝나므로, 뒤에서부터 1의 위치를 찾고, 그 앞의 56자리 추출
            last_idx = ''.join(map(str, line)).rfind('1')
            target_code = line[last_idx - 55 : last_idx + 1]
            break
    # 2. 해독한다
    print(f'#{test_case} {is_valid(target_code)}')
