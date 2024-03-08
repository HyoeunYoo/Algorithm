# [백준] 1158번 - 요세푸스 문제 (실버 4)
# 큐 활용
# 2024.03.06 - 34016 KB / 2028 ms
# [O] 구현 / 자료구조 / 큐

from collections import deque

# 입력
N, K = map(int, input().split())

# 맨 처음 앉아있는 사람들 - 큐
queue = deque(range(1, N + 1))

# 요세푸스 순열
result = []

# 큐가 빌 때까지 반복
while queue:
    # 큐에서 K-1번 pop → push
    for _ in range(K-1):
        queue.append(queue.popleft())

    # 큐에서 1번 pop한 데이터를 요세푸스 순열에 추가
    result.append(queue.popleft())

# 결과 출력
print(str(result).replace("[", "<").replace("]",">"))