# [백준] 2667번 - 단지번호 붙이기 (실버 1)
# 2024.03.23 - 34096 KB / 64 ms
# [O] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색 / 깊이 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
    
complex = []  # 단지

# 상하좌우 계산을 위한 데이터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
    
# BFS 함수
def bfs(x, y):
    home = 0  # 집의 수
    queue = deque([(x, y)])
    
    # 시작 위치 0으로 변경
    graph[x][y] = 0
    home += 1
    
    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 이동하면서 인접한 1을 모두 0으로 변경
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이동한 위치가 범위를 벗어나면 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                home += 1
                
    return home

# 집, 단지의 수 구하기
for i in range(N):
    for j in range(N):
        # 데이터가 1이면 BFS를 수행하여 인접한 1을 모두 0으로 변경
        if graph[i][j] == 1:
            complex.append(bfs(i, j))
            
print(len(complex))
for i in sorted(complex):
    print(i)