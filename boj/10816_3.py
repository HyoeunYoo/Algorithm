# [백준] 10816번 - 숫자 카드 2 (실버 4)
# 정렬, bisect 라이브러리
# 2024.03.15 - 118744 KB / 1496 ms
# [-] 자료구조 / 정렬 / 이분탐색 / 해시를 사용한 집합과 맵

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 입력
N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

# N개의 정수 오름차순 정렬
nlist.sort()

# [left_value, right_value] 범위에 속하는 값의 개수를 반환하는 함수
# left_value == right_value 라면 이 값의 개수를 반환한다.
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

for m in mlist:
    # m의 개수 계산
    count = count_by_range(nlist, m, m)
    print(count, end = ' ')