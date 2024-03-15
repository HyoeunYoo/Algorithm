# [백준] 18870번 - 좌표 압축 (실버 2)
# 2024.03.16 - 143264 KB / 1848 ms
# [O] 정렬 / 값 / 좌표 압축

import sys
input = sys.stdin.readline

# 입력
N = int(input())
list1 = list(map(int, input().split()))

# 중복 제거, 정렬
list2 = sorted(list(set(list1)))

# {좌표: list2에서의 인덱스} 딕셔너리
dic = {}    
for idx, x in enumerate(list2):
    dic[x] = idx

for x in list1:
    print(dic.get(x), end = ' ')