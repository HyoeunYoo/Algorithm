# [백준] 1012번 - 유기농 배추 (실버 2)
# 2024.03.22 - 34096 KB / 72 ms
# [O] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색 / 깊이 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

# 상하좌우 계산을 위한 데이터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수
def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    
    # 시작 위치 0으로 변경
    graph[a][b] = 0
    
    while q:
        x, y = q.popleft()
        
        # 상하좌우 이동하면서 인접한 1을 모두 0으로 변경
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이동한 위치가 범위를 벗어나면 패스
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())
    
    # N * M 크기의 인접 행렬
    graph = [[0] * M for _ in range(N)]
    
    # 배추의 위치 1로
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    # 지렁이 수 구하기
    count = 0
    for y in range(N):
        for x in range(M):
            # 데이터가 1이면 BFS를 수행하여 인접한 1을 모두 0으로 변경
            if graph[y][x] == 1:
                bfs(graph, y, x)
                count += 1
    
    print(count)