import heapq
from collections import defaultdict

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def kruskal(V, edges):
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


def prim(V, edges):
    '''
        주어진 그래프에서 최소신장트리를 찾고 mst를 구성하는 간선의 가중치를 모두 더하기
        param : V : 노드의 개수, edges : 간선의 정보
        kruskal : 가장 작은 간선부터 선택해서 트리를 구성
        prim : 임의의 정점에서 부터 시작해서 우선순위큐를 이용해 작은 가중치를 가진 간선을 선택
    '''
    '''
        prim:
        1. 임의의 정점에서 우선순위 큐를 사용해 연결된 간선을 가중치 오름차순으로 정렬 -> 우선순위 큐에 넣을거라 필요업ㅅ
        2. 가장 작은것을 선택한 후, 연결된 곳으로 이동해 다시 연결된 간선들을 우선순위 큐에 삽입
        3. 이때, 이미 방문한 노드의 경우 포함하지 않음.
        4. 우선순위 큐가 빌 때까지 반복함.
    '''
    # prim
    # 우선순위 큐를 사용

    # [방어 코드 1] 노드가 1개 이하면 MST 비용은 0
    if V <= 1:
        return 0
    # [방어 코드 2] 간선이 없으면 MST 생성 불가 (V>1일 경우)
    if not edges:
        return -1 # 또는 문제에서 요구하는 오류 값

    # 방문노드 저장, 임의의 시작 노드 지정
    start_node = 1
    visited = set([1])

    mst = []

    # 무향 그래프 인접리스트 생성
    adj_list = {v: [] for v in range(1,V+1)}
    # print(adj_list)
    for s, e, w in edges:
        adj_list[s].append([e,w])
        adj_list[e].append([s,w])
    # print(adj_list)    
    # 임의의 정점에서 나오는 모든 간선들을 list에 넣고 우선순위 큐에 넣음
    min_heap = [[w, start_node, e] for e, w in adj_list[start_node]]
    # print(min_heap)
    heapq.heapify(min_heap)
    # print(min_heap)

    while min_heap: # 모든 간선 순회
        w,s,e = heapq.heappop(min_heap)

        # end 노드를 방문하지 않았다면
        if e not in visited:
            visited.add(e)
            mst.append([s,e,w])
            # end node에 연결된 간선들 heapq에 넣음
            for next, weight in adj_list[e]:
                # end node -> next에서 방문하지 않은 next만 선택
                if next not in visited:
                    heapq.heappush(min_heap, [weight, e, next])

    # [방어 코드 3] 모든 노드를 방문했는지 최종 확인
    if len(visited) == V:
        return mst
    else:
        # MST를 완성하지 못한 경우 (그래프가 분리됨)
        return -1 # 또는 문제에서 요구하는 오류 값



for tc in range(1,T+1):
    # V 노드개수, E 간선 개수
    V, E = map(int, input().split())

    # 간선 정보 , start, end, weight
    edges = [list(map(int, input().split())) for _ in range(E)]

    mst = prim(V, edges)
    # print('mst',mst)
    value = [w[2] for w in mst]
    print(f'#{tc} {sum(value)}')