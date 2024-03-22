# [백준] 11724번 - 연결 요소의 개수 (실버 2)
# DFS 이용
# 2024.03.23 - 73056 KB / 736 ms
# [O] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색 / 깊이 우선 탐색

import sys
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

# DFS 함수
def dfs(start):
    stack = [start]
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            stack.extend(reversed(graph[v]))

# 모두 방문할 때 까지 dfs 수행
while False in visited:
    v = visited.index(False)
    dfs(v)
    conn += 1

print(conn)