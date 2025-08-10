import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def make_postexpr(expr):
    postexpr = []
    stack = []
    for exp in expr:
        # 숫자면 후위표기식에 넣고
        if str(exp).isnumeric():
            postexpr.append(exp)
        else:
            # 아닐때는 stack에 연산자가 있는지 확인 후
            if stack:
                # 있으면 stack에 있는 연산자를 pop해서 후위 표기식에 넣고
                postexpr.append(stack.pop())
                stack.append(exp)
            else:
                # 없으면 stack에 넣음
                stack.append(exp)
    
    postexpr.append(stack.pop())
    return postexpr

def do_postoperator(postexpr):
    stack = []
    for ex in postexpr:
        if str(ex).isnumeric():
            stack.append(ex)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a)+int(b))
    return stack[-1]

for test_case in range(1,11):
    L = int(input()) # 문자열 길이
    expr = list(input()) # 계산식
    postexpr = make_postexpr(expr)
    
    print(f'#{test_case} {do_postoperator(postexpr)}')