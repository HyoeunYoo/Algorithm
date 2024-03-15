# [백준] 1920번 - 수 찾기 (실버 4)
# 집합(set)
# 2024.03.16 - 50520 KB / 180 ms
# [-] 자료구조 / 정렬 / 이분탐색

import sys
input = sys.stdin.readline

# 입력
N = int(input())
nset = set(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

for m in mlist:
    print(1 if m in nset else 0)