import sys

sys.stdin = open('input.txt', 'r')

# n,s극이 붙어있는것을 하나의 교착상태로 본다
# 만약 각각 두개의 n,s극이 번갈아가며 있으면 두개로 본다.
# 1. 맨 위에 2이면 out.
# 2. 맨 아래에 1이면 out.
# 3. s극과 n극이 처음 만나면 교착상태.
#   3-1. 
# 1이 N극, 2가 S극
for test_case in range(1,11):
    length = int(input())
    table = [list(map(int, input().split())) for _ in range(length)]


    for line in zip(*table):
        stack = [x for x in line if x > 0]
        print(stack)
        # stack.reverse()
        # while stack:
        #     top = stack.pop()
        #     if top == 1