import sys
from collections import defaultdict
import heapq 

sys.stdin = open('sample_input.txt', 'r')
t = int(input())

def dijkstra(graph):
    # 시작정점에서 해당 노드까지 도달하는 거리 초기화
    distance = [float('inf')] * (N+1) # 0~N개의 노드 총 N + 1개
    # 시작정점 거리 초기화
    distance[0] = 0
 
    # 최소힙 생성
    heap = []
    # 지금까지의 거리와 헤당 정점을 heap에 추가
    # 초기값이기 때문에 거리 0
    heapq.heappush(heap, (0,0))

    while heap:
            # 현재 가장 짧은 거리를 가진 노드를 꺼냄
            current_dist, current_node = heapq.heappop(heap)
            
            # 이미 처리된 노드라면 무시
            # (힙에 저장된 거리보다 더 짧은 경로가 이미 발견되었다면 스킵)
            if distance[current_node] < current_dist:
                continue
                
            # 현재 노드와 연결된 인접 노드들을 확인
            for next_node, weight in graph[current_node]:
                # 현재 노드를 거쳐 가는 새로운 경로의 거리
                new_dist = current_dist + weight
                
                # 새로운 경로가 기존 경로보다 짧다면 거리 갱신 및 힙에 추가
                if new_dist < distance[next_node]:
                    distance[next_node] = new_dist
                    heapq.heappush(heap, (new_dist, next_node))
                    
    return distance

for tc in range(1,t+1):

    # 노드의 개수 N, 도로의 개수 E
    N, E = map(int, input().split())

    # i에서 j까지의 비용 인접행렬
    edges = [list(map(int, input().split())) for _ in range(E)]

    graph = defaultdict(list)

    # 간선 정보를 순회하며 딕셔너리에 추가
    for u, v, weight in edges:
        graph[u].append((v, weight))

    # pprint.pprint(dict(graph))
    distance = dijkstra(graph)

    print(f'#{tc} {distance[-1]}')