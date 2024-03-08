# [백준] 9012번 - 괄호 (실버 4)
# 2024.03.09 - 31120 KB / 44 ms
# [O] 자료구조 / 문자열 / 스택

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    input = list(sys.stdin.readline().strip())
    stack = []
    
    for i in input:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop() 
            else:
                stack.append(i)
                break
    
    print("NO" if stack else "YES")