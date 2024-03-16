# [프로그래머스] 입국심사 (레벨 3)
# 2024.03.16 - 최대 14 KB / 575.21 ms
# [O] 이분탐색

def solution(n, times):
    answer = 0
    
    start, end = 1, n * max(times)
    
    while start <= end:
        mid = (start + end) // 2
        
        # 모든 심사관들이 mid분 동안 심사한 사람의 수
        check = 0
        for t in times:
            check += mid // t
            
            if check > n:
                break
        
        if check >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer