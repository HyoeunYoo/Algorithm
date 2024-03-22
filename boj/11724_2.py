# [백준] 11724번 - 연결 요소의 개수 (실버 2)
# BFS 이용
# 2024.03.23 - 65120 KB / 688 ms
# [-] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색 / 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 그래프 변환
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [True] + [False] * N  # 방문 확인
conn = 0  # 연결 요소의 개수

# BFS 함수
def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 모두 방문할 때 까지 bfs 수행
while False in visited:
    v = visited.index(False)
    bfs(v)
    conn += 1

print(conn)