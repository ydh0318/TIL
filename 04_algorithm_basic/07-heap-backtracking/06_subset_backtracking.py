def find_subset(start, current_subset, current_sum):
    global cnt
    cnt += 1
    # 가지치기 하나 더 추가
    if current_sum > target_sum:
        return  # 더이상 조사 의미없음

    print(current_subset, current_sum)
    # 현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        # 원본 그대로 넣으면 복제본이 들어가서 곤란하므로
        # 새로운 리스트 만들어서 집어넣기
        result.append(list(current_subset))
        # result.append(current_subset[:])
        return
    # start부터 전체 수를 다 순회
    for idx in range(start, len(nums)):
        num = nums[idx]
        # 현재 선택한 수를 집합에 넣고, 값도 추가해서 다음작업
        current_subset.append(num)
        find_subset(idx + 1, current_subset, current_sum + num)
        current_subset.pop()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target_sum = 20
cnt = 0
result = []
# 필요한 인자들은?
# 1. 재귀를 중단시킬 파라미터 (총합이 10이 되면 종료)
# 2. 누적해서 가야가야할 파라미터 -> 만들어지는 부분집합
# + 그 선택할 집합의 index 파라미터
find_subset(start=0, current_subset=[], current_sum=0)
print(result)
print(cnt)
