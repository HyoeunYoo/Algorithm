# [백준] 2805번 - 나무 자르기 (실버 2)
# 이진 탐색 - 재귀 함수
# 2024.03.16 - 143264 KB / 2204 ms
# [O] 이분탐색 / 매개 변수 탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

# 이진 탐색 재귀 함수
def binary_search(start, end):
    # start가 end보다 커지면 최종 end 값이 H의 최댓값이다.
    if start > end:
        return end
        
    H = (start + end) // 2
    
    # 자르고 남은 나무 길이의 합
    sum = 0
    for t in tree:
        if t > H:
            sum += t - H
    
    if sum == M:
        return H
    elif sum > M:
        return binary_search(H + 1, end)
    else:
        return binary_search(start, H - 1)

print(binary_search(0, max(tree)))