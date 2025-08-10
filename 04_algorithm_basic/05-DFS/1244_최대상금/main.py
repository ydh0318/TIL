import sys
sys.stdin = open('input.txt')

def dfs(change_count):
    global max_number
    
    # 교환 다 했으면
    if change_count == exchange:
        current_number = int(''.join(map(str, cards)))
        max_number = max(current_number, max_number)
        return
    
    # 현재 상태 : 교환 횟수, 현재 숫자
    current_state = (change_count, int(''.join(map(str, cards))))
    # 가지치기 : 만약 현재 교환 숫자에 현재 숫자가 있다면 return
    if current_state in visited:
        return
    visited.add(current_state)
    
    # 교환
    for i in range(len(cards)):
        for j in range(len(cards)):
            if i != j:
                cards[i], cards[j] = cards[j], cards[i]
                dfs(change_count + 1)
                cards[i], cards[j] = cards[j], cards[i]


T = int(input())

for tc in range(1, T+1):
    cards, exchange = input().split()
    exchange = int(exchange)
    cards = list(map(int, cards))
    max_number = 0
    #print(cards, exchange)
    visited = set()
    dfs(0)
        
    print(f'#{tc} {max_number}')