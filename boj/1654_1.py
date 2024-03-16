# [백준] 1654번 - 랜선 자르기 (실버 2)
# 2024.03.16 - 31120 KB / 96 ms
# [X] 이분탐색 / 매개 변수 탐색

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for l in lan:
        count += (l // mid)
        if count > N:
            break
    
    # 틀린 부분
    # if N == count:
    #     end = mid
    #     break
    
    if N > count:
        end = mid - 1
    else:
        start = mid + 1

print(end)