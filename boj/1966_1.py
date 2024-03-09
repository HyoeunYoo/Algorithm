# [백준] 1966번 - 프린터 큐 (실버 3)
# 2024.03.09 - 34036 KB / 84 ms
# [O] 구현 / 자료구조 / 시뮬레이션 / 큐

import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # 문서의 개수, 답을 구하려는 문서의 현재 순번
    N, M = map(int, input().split())
    
    # 문서 큐(순번, 중요도)
    queue = deque(tuple(enumerate(map(int, input().split()))))
    
    # 인쇄된 순번
    count = 0
    
    while queue:
        # 가장 높은 중요도 연산
        max_imp = max(i[1] for i in queue)
        
        tmp = queue.popleft()
        if tmp[1] == max_imp:
            count += 1
            if tmp[0] == M:
                print(count)
                break
        else:
            queue.append(tmp)