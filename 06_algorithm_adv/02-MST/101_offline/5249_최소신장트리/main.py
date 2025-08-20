import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def MST(V, edges):
    '''
        주어진 그래프에서 최소신장트리를 찾고 mst를 구성하는 간선의 가중치를 모두 더하기
        param : V : 노드의 개수, edges : 간선의 정보
        kruskal : 가장 작은 간선부터 선택해서 트리를 구성
        prim : 임의의 정점에서 부터 시작해서 우선순위큐를 이용해 작은 가중치를 가진 간선을 선택
    '''
    '''
        kruskal:
        1. 가중치를 기준으로 오름차순 정렬
        2. 서로소 집합을 생성
        3. 간성정보순회하며 union
            3-1. union시 루트가 같으면 사이클 생성함.
    '''
    '''
        prim:
        1. 임의의 정점에서 우선순위 큐를 사용해 연결된 간선을 가중치 오름차순으로 정렬
        2. 가장 작은것을 선택한 후, 연결된 곳으로 이동해 다시 연결된 간선들을 우선순위 큐에 삽입
        3. 이때, 이미 방문한 노드의 경우 포함하지 않음.
        4. 우선순위 큐가 빌 때까지 반복함.
    '''
    # kruskal
    # 서로소 집합 생성
    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    # 간선정보순회하며 union 생성
    # 이때 간선을 가중치 오름차순으로 정렬
    edges.sort(key=lambda x : x[2])
    def find_set(x):
        if x != parent[x]:
            x = find_set(parent[x])
        return parent[x]
    def union_set(x,y):
        root_x = find_set(x)
        root_y = find_set(y)
        if root_x != root_y: # 루트노드가 다르면 다른 서로소 집합임
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_y] > rank[root_x]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    # mst 생성
    mst = []

    for s, e, w in edges:
        # 두 간선의 root가 다르면 union하고 간선 정보 mst에 추가함.
        if find_set(s) != find_set(e):
            union_set(s,e)
            mst.append([s,e,w])
    return mst


for tc in range(1,T+1):
    # V 노드개수, E 간선 개수
    V, E = map(int, input().split())

    # 간선 정보 , start, end, weight
    edges = [list(map(int, input().split())) for _ in range(E)]

    mst = MST(V, edges)
    # print(mst)
    value = [w[2] for w in mst]
    print(f'#{tc} {sum(value)}')