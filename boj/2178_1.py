# [백준] 2178번 - 미로 탐색 (실버 1)
# 2024.03.23 - 34068 KB / 80 ms
# [O] 그래프 이론 / 그래프 탐색 / 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# 미로
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))
    
# 상하좌우 계산을 위한 데이터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작 위치
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    
    # 상하좌우 칸 계산
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 이동할 칸이 범위 내, 1이면 이동한 칸 수 저장
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
            q.append((nx, ny))
            maze[nx][ny] = maze[x][y] + 1

# N, M 위치의 칸 수 출력
print(maze[N-1][M-1])