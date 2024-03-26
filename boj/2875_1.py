# [백준] 2875번 - 대회 or 인턴 (브론즈 3)
# 2024.03.26 - 31120 KB / 40 ms
# [O] 수학 / 구현 / 사칙연산

N, M, K = map(int, input().split())

team = N // 2

if team > M:
    team = M
    N -= team * 2
    M = 0
else:
    N %= 2
    M -= team

while K > N + M:
    team -= 1
    N +=2
    M += 1

print(team)