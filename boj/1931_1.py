# [백준] 1931번 - 회의실 배정 (실버 1)
# 2024.03.29 - 51900 KB / 236 ms
# [X] 그리디 알고리즘 / 정렬

import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 기준 오름 차순 정렬 후 시작 시간 기준 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 첫번째 회의 선택하고 제거
start, end = meetings[0]
del meetings[0]
count = 1

for next_start, next_end in meetings:
    # 다음 회의 시작 시간이 현재 회의 끝나는 시간 이후이면 선택
    if end <= next_start:
        start, end = next_start, next_end
        count += 1
    
print(count)