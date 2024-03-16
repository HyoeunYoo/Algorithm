# [백준] 2805번 - 나무 자르기 (실버 2)
# 이진 탐색 - 반복문
# 2024.03.16 - 150200 KB / 4820 ms
# [-] 이분탐색 / 매개 변수 탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
    sum = 0
    H = (start + end) // 2
    
    for t in tree:
        if t > H:
            sum += t - H
    
    if sum < M:
        end = H - 1
    else:
        start = H + 1
        
print(end)