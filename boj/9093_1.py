# [백준] 9093번 - 단어 뒤집기 (브론즈 1)
# 2024.03.09 - 31120 KB / 128 ms
# [O] 구현 / 문자열

import sys

input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    sentence = list(list(word) for word in input().split())
    
    # 단어 뒤집기
    for word in sentence:
        word.reverse()
    
    print(' '.join(''.join(word) for word in sentence))