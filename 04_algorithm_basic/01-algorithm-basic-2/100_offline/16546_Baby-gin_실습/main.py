# triplet인 경우
# 똑같은 숫자가 세개 혹은 연속된 숫자가 세개
# 두가지 경우
# 1. 같은 숫자 찾은 후, 연속된 숫자 찾기
# 2. 연속된 숫자를 찾은 후, 같은 숫자 찾기
# ps ) 정렬 순서도 고려

def is_babygin(card):
    #1. 앞의 3개 확인
    first_number = card[0]
    is_same_front = True
    is_sequential_front = True
    for i in range(3):
    # 같은 숫자인지 확인
        if card[i] != card[0]:
            is_same_front = False
            break
    for i in range(3):
    # 연속된 숫자인지 확인
        if card[i] != first_number:
            is_sequential_front = False
            break
        first_number += 1
        
    is_same_back = True
    is_sequential_back = True
    #2. 뒤의 3개 확인
    first_number = card[3]
    for i in range(3):
    # 같은 숫자인지 확인
        if card[i] != card[3]:
            is_same_back = False
            break
        if card[i] != first_number:
            is_sequential_back = False
            break
        first_number += 1

    return (is_same_front | is_sequential_front) & (is_same_back | is_sequential_back)
    

N = int(input())
cards = [list(map(int, input().strip())) for _ in range(N)]

# for _ in range(N):
#     card = list(map(int, input().strip()))
#     # 1. 정렬
idx = 1
for card in cards:
    raw = is_babygin(card)
    # sc = sorted(card)
    # print(sc)
    sorted_card = is_babygin(sorted(card))
    print(f'#{idx} {str(raw | sorted_card).lower()}')
    idx += 1

