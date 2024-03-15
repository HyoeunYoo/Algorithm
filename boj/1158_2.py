# [백준] 1158번 - 요세푸스 문제 (실버 4)
# 리스트 인덱스 활용
# 2024.03.06 - 31120 KB / 52 ms
# [-] 구현 / 자료구조 / 큐

# 입력
N, K = map(int, input().split())

# 맨 처음 앉아있는 사람들 - 리스트
arr = [i for i in range(1, N + 1)]

# 제거할 사람 인덱스
idx = 0

# 요세푸스 순열
result = []

# K 주기의 데이터를 K-1 주기의 인덱스로 제거
for _ in range(N):
    idx += K - 1
    
    if idx >= len(arr):
        idx %= len(arr)
        
    result.append(str(arr.pop(idx)))

# 결과 출력
print("<", ", ".join(result), ">", sep="")