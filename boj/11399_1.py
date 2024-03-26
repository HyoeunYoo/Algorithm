# [백준] 11399번 - ATM (실버 4)
# 2024.03.27 - 31120 KB / 44 ms
# [O] 그리디 알고리즘 / 정렬

N = int(input())
P = sorted(list(map(int, input().split())))

result = 0
for i in range(1, N + 1):
    result += P[-i] * i

print(result)