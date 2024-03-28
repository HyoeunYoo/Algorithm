# [백준] 12845번 - 모두의 마블 (실버 3)
# 2024.03.28 - 31120 KB / 40 ms
# [O] 그리디 알고리즘

n = int(input())
lvs = list(map(int, input().split()))

# 가장 높은 레벨
max = max(lvs)
max_idx = lvs.index(max)

gold = 0
    
for idx, lv in enumerate(lvs):
    if idx == max_idx:
        continue
    gold += max + lv
    
print(gold)