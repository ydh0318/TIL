import heapq, math


def dijkstra(graph, start):
    distances = {v: math.inf for v in graph}
    distances[start] = 0 # 시작 정점까지 도달하는 거리 0 초기화
    # 내 다음 조사 후보군들을 삽입할 배열
    heap = []   # 최소 힙
    heapq.heappush(heap, [0, start])    # [도달한 거리, 시작정점]
    visited = set()
    visited.add(start)

    while heap:
        # print(heap)
        # print(distances)
        dist, current = heapq.heappop(heap)
        # 기존 거리보다, 갱신된 거리가 더 크고, 이미 방문한적 있으면 패스
        if current in visited or distances[current] < dist: continue
        visited.add(current)

        # 현재 노드 기준 인접한 모든 노드에 대해서, 갱신하거나, 우선순위큐에 삽입
        for next, weight in graph[current].items():
            next_distance = dist + weight   # 현재까지 걸린 가중치 + 다음 위치까지의 가중치
            # 아직 방문하지 않았고, 정점까지 도달하는 거리가 충분히 작을때
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])
    return distances

graph = {
    'a': {'b': 3, 'c': 5},
    'b': {'c': 2},
    'c': {'b': 1, 'd': 4, 'e': 6},
    # 'c': {'b': -4, 'd': 4, 'e': 6},
    'd': {'e': 2, 'f': 3},
    'e': {'f': 6},
    'f': {}
}
start_v = 'a'
res = dijkstra(graph, start_v)
print(res)  # {'a': 0, 'b': 3, 'c': 5, 'd': 9, 'e': 11, 'f': 12}

