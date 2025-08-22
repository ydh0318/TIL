
import sys
sys.stdin = open('sample_input.txt', 'r')



def make_set(N):
        '''
            N+1길이의 parent 배열과 rank 배열 리턴
        '''
        parent = [i for i in range(N+1)]
        rank = [0] * (N+1)  #   모든 집합의 rank를 0으로 초기화
        return parent, rank

def find_set(x):
    # 경로 압축
    # 루트노드가 아니면
    if x != parent[x]:
        # 찾아낸 대표자를 부모로 갱신함
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
    
    # N명의 사람과 M장의 신청자
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    parent, rank = make_set(N)

    for i in range(0,M*2,2):
        union_set(paper[i], paper[i+1])
        
    groups = set()
    for i in range(1, N + 1):
        # 합집합 시 find_set을 수행하지 않은 노드들은 parent 배열이 갱신되지 않기 때문에,
        groups.add(find_set(i)) # find_set을 통해 최종 대표자를 구해야 함

    # 최종 대표자의 개수가 곧 그룹의 개수
    print(f'#{tc} {len(groups)}')