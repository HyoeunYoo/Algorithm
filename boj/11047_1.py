# [백준] 11047번 - 동전 0 (실버 4)
# 2024.03.28 - 31252 KB / 40 ms
# [O] 그리디 알고리즘

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_types = reversed(list(int(input()) for _ in range(N)))

count = 0
for coin in coin_types:
    count += K // coin
    K %= coin

print(count)