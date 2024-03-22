# [백준] 1260번 - DFS와 BFS (실버 2)
# 인접 행렬
# 2024.03.20 - 39504 KB / 548 ms
# [-] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색 / 깊이 우선 탐색

from collections import deque

# 입력
N, M, V = map(int, input().split())

# 그래프로 변환 - 연결 여부 인접 행렬
graph = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


# DFS 함수
visited_dfs = [False] * (N + 1)
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    
    for i in range(1, N + 1):
        # i 노드를 방문하지 않았고 V와 연결되어 있다면 재귀
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)


# BFS 함수
def bfs():
    visited_bfs = [False] * (N + 1)
    visited_bfs[V] = True
    queue = deque([V])
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in range(1, N + 1):
            # i 노드를 방문하지 않았고 V와 연결되어 있다면
            if not visited_bfs[i] and graph[v][i]:
                visited_bfs[i] = True
                queue.append(i)


dfs(V)
print()
bfs()