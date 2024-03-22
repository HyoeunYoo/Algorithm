# [백준] 1260번 - DFS와 BFS (실버 2)
# 인접 리스트, 정렬
# 2024.03.20 - 34068 KB / 76 ms
# [O] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색 / 깊이 우선 탐색

import sys
from collections import deque

# 입력
input = sys.stdin.readline
N, M, V = map(int, input().split())

# 그래프로 변환 - 노드 번호 인접 리스트
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()


# DFS 함수
visited_dfs = [False] * len(graph)
def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)


# BFS 함수
def bfs():
    visited_bfs = [False] * len(graph)
    visited_bfs[V] = True
    queue = deque([V])
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)


dfs(V)
print()
bfs()