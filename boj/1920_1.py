# [백준] 1920번 - 수 찾기 (실버 4)
# 정렬, 이진 탐색
# 2024.03.16 - 47408 KB / 488 ms
# [O] 자료구조 / 정렬 / 이분탐색

import sys
input = sys.stdin.readline

# 입력
N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

# 정렬
nlist.sort()

# 이진 탐색 재귀 함수
def binary_search(target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if nlist[mid] == target:
        return 1
    elif nlist[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)
    
for m in mlist:
    print(binary_search(m, 0, N - 1))