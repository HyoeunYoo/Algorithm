# [백준] 10816번 - 숫자 카드 2 (실버 4)
# 딕셔너리 키
# 2024.03.15 - 119748 KB / 840 ms
# [-] 자료구조 / 정렬 / 이분탐색 / 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

# 입력
N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

# {정수: 개수} 딕셔너리
count = {}
for n in nlist:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

# 딕셔너리 key 중에서 정수 검색하여 개수(value) 출력
for m in mlist:
    target = count.get(m)
    print(0, end = ' ') if target == None else print(target, end = ' ')