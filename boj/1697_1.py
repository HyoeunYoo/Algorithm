# [백준] 1697번 - 숨바꼭질 (실버 1)
# 2024.03.23 - 35288 KB / 132 ms
# [O] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100000  # 범위
visited = [0] * (MAX + 1)  # 방문 초 배열
q = deque([N])

while q:
    v = q.popleft()
    
    # 찾을 위치와 같다면 방문 초 출력
    if v == K:
        print(visited[K])
        break
    
    # -1, 1, *2 만큼 이동하고 중복 제거
    for i in (v - 1, v + 1, v * 2):
        # 범위 내 노드 중 방문하지 않은 노드를 큐에 삽입, 방문 초 저장
        if 0 <= i <= MAX and visited[i] == 0:
            q.append(i)
            visited[i] = visited[v] + 1