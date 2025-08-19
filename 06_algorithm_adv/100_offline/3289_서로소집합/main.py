import sys
sys.stdin = open('sample_input.txt','r')

def make_set(N):
        '''
            N+1길이의 parent 배열과 rank 배열 리턴
        '''
        parent = [i for i in range(N+1)]
        rank = [0] * (N+1)  #   모든 집합의 rank를 0으로 초기화
        return parent, rank

def find_set(x):
    # 만약 루트노드가 아니면
    if parent[x] != x:
        # 부모노드의 부모를 찾아서 위에서 부터 초기화 시켜줌
        parent[x] = find_set(parent[x])
    return parent[x]

def union_set(x,y): # x가 포함된 집합에 y집합을 추가
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y: # 루트가 다르다면 합집합 수행
        # 랭크를 고려함
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            parent[root_x] = root_y
        else: # 랭크가 똑같다면 상황에 따라 달라짐
            parent[root_y] = root_x
            rank[root_x] += 1

t = int(input())

for tc in range(1, t+1):
    
    N, M = map(int, input().split())
    operation = [list(map(int, input().split())) for _ in range(M)]
    parent, rank = make_set(N)
    result = ''
    for i in range(M):
        if operation[i][0] == 0: # 합집합 연산
            union_set(operation[i][1], operation[i][2])
        elif operation[i][0] == 1: # 같은 집합에 포함되어 있는지 확인
            if find_set(operation[i][1]) == find_set(operation[i][2]):
                result += '1'
            else:
                result += '0'

    print(f'#{tc} {result}')