# [백준] 10828번 - 스택 (실버 4)
# 2024.03.05 - 31120 KB / 48 ms
# [O] 구현 / 자료구조 / 스택

import sys

# 명령의 수
N = int(sys.stdin.readline())

# 스택 초기화
stack = []

# 명령 처리
for _ in range(N):
    cmd = sys.stdin.readline()
    
    if 'push' in cmd :
        stack.append(int(cmd.split()[1]))
    elif 'pop' in cmd :
        print(stack.pop()) if stack else print(-1)
    elif 'size' in cmd :
        print(len(stack))
    elif 'empty' in cmd :
        print(0) if stack else print(1)
    elif 'top' in cmd :
        print (stack[-1]) if stack else print(-1)