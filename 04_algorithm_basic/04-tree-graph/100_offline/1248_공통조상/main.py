import sys
from collections import defaultdict

sys.stdin = open('input.txt')

def dfs(root, depth, route):
    global subtree
    # 종료조건
    if root == vertex1: 
        result.append(route[:])
        return
    if root == vertex2:
        result.append(route[:])
        return
    
    # 자식 있다면 순회
    if adj_list[root]:
        for child in adj_list[root]:
            route.append(child)
            dfs(child, depth+1, route)
            route.pop()
        

T = int(input())

for tc in range(1, T+1):
    # 정점 개수, 간선 개수, 정점1, 정점2
    V, E, vertex1, vertex2 = map(int, input().split())
    edges = list(map(int, input().split()))
    result = []
    
    adj_list = defaultdict(list)
    for i in range(0,len(edges),2):
        adj_list[edges[i]].append(edges[i+1])
    
    dfs(1,0,[1])
    same = [x for x in result[0] if x in result[1]]

    count = 1
    def count_subtree(root):
        global count
        for child in adj_list[root]:
            count += 1
            count_subtree(child)
    count_subtree(same[-1])

    print(f'#{tc} {same[-1]} {count}')
