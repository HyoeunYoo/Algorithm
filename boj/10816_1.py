# [백준] 10816번 - 숫자 카드 2 (실버 4)
# 정렬, 딕셔너리, 이진 탐색
# 2024.03.15 - 119780 KB / 2920 ms
# [O] 자료구조 / 정렬 / 이분탐색 / 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

# 입력
N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

# N개의 정수 오름차순 정렬
nlist.sort()

# {정수: 개수} 딕셔너리
count = {}
for n in nlist:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

# 이진 탐색 재귀 함수
def binary_search(target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    
    if nlist[mid] == target:
        return count[m]
    elif nlist[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)

# M개의 정수를 이진 탐색
for m in mlist:
    print(binary_search(m, 0, N - 1), end=' ')