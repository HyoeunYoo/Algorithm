# [백준] 10610번 - 30 (실버 4)
# 2024.03.28 - 33036 KB / 248 ms
# [O] 수학 / 그리디 알고리즘 / 문자열 / 정렬 /정수론

N = sorted(list(input()), reverse=True)

max = int(''.join(N))

print(max) if max % 30 == 0 else print(-1)