def perm_no_slice(arr, start_idx):
    '''
    Args:
        arr: 순열을 만들 원본 리스트 (여기서는 변경 가능)
        start_idx: 현재 순열을 만들고 있는 시작 인덱스
    '''
    if start_idx == 2:
        print(arr[:2])
    if start_idx == len(arr):
       # print(arr)
       return
    # 재귀호출
    for idx in range(start_idx, len(arr)):
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]
        perm_no_slice(arr, start_idx + 1)
        # 원래 배열로 되돌림
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]


# 사용 예시
my_list = [1, 2, 3]
perm_no_slice(my_list, 0)