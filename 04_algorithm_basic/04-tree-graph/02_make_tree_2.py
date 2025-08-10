# 부모의 정보만 주어질 때, 이진 트리 생성하기
# 자신의 값, 부모 인덱스 (부모가 0인 경우, 루트)
input_data = [
    ['A', 0],
    ['C', 1],
    ['B', 1],
    ['F', 3],
    ['G', 6],
    ['E', 2],
    ['D', 2]
]

N = 16
tree = [0] * (N+1)
print(tree)

for data in input_data:
    print(data)
    value = data[0]     # A
    parent = data[1]    # 0

    # 자식 인덱스 계산
    left_child = parent * 2
    right_child = parent * 2 + 1

    # 내 부모가 없다. -> 0이다. -> 아, 내가 루트 노드다.
    if not parent:
        tree[1] = value     # 루트 노드 위치에 나를 삽입하고,
        continue            # 다음 for문으로 넘긴다.

    # 나에게 주어진 정보가 부모 노드의 index 뿐이니,
    # 내가 이진트리에서 어디에 삽입될 수 있는지를 보려면,
    # 당연하게도, 부모 노드의 왼쪽 자식, 오른쪽 자식중, 비어있는 곳을 찾아야한다.
    if not tree[left_child]:
        tree[left_child] = value
    else:
        tree[right_child] = value
print(tree)