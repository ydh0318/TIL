import sys
sys.stdin = open('sample_input.txt', 'r')

def floyd_warshall(graph):
    n = len(graph)  # 전체 노드의 개수
    # 모든 정점을 경유 정점으로 고려
    for k_node in range(n): # k를 거쳐서 감
        for start in range(n): # 시작노드
            for end in range(n): # 도착노드
                # Dik + Dkj < Dij
                Dik = graph[start][k_node]  # i에서 k로 가는 거리
                Dkj = graph[k_node][end]    # k에서 j로 가는 거리
                Dij = graph[start][end]     # i에서 j로 가는 거리
                if Dik + Dkj < Dij:         # k를 경유하는게 더 싸면
                    graph[start][end] = Dik + Dkj   # 그걸로 갱신
    # 음수 사이클 확인
    # for i in range(n):
    #     if graph[i][i] < 0:
    #         print('음수 사이클이 존재함')
    #         break
    
    return graph

t = int(input())

for tc in range(1,t+1):

    # 노드의 개수 N
    N = int(input())

    # i에서 j까지의 비용 인접행렬
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i!=j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = float('inf')
                
    # print(adj_matrix)
    result = floyd_warshall(adj_matrix)

    answer = -99
    for row in result:
        answer = max(answer, max(row))

    print(f'#{tc} {answer}')