# [백준] 10828번 - 스택 (실버 4)
# 조건 1. 입력을 모두 받고 난 후에 출력하기
# 2024.03.05 - 32140 KB / 52 ms
# [O] 구현 / 자료구조 / 스택

import sys

# 명령의 수
N = int(sys.stdin.readline())

# 명령 리스트
cmds = [sys.stdin.readline().strip() for _ in range(N)]

# 스택 초기화
stack = []

# 명령 처리
for cmd in cmds:
    if cmd.split()[0] == 'push' :
        stack.append(int(cmd.split()[1]))
    elif cmd == 'pop' :
        print(stack.pop()) if stack else print(-1)
    elif cmd == 'size' :
        print(len(stack))
    elif cmd == 'empty' :
        print(0) if stack else print(1)
    elif cmd == 'top' :
        print (stack[-1]) if stack else print(-1)