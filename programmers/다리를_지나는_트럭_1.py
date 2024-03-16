# [프로그래머스] 다리를 지나는 트럭 (레벨 2)
# 2024.03.08 - 최대 10400 KB / 53.63 ms
# [O] 스택/큐

from collections import deque

def solution(bridge_length, weight, truck_weights):    
    answer = 0  # 시간
    
    crossing = deque([0] * bridge_length)  # 다리를 건너는 트럭 - 큐
    waiting = deque(truck_weights)  # 대기 트럭 - 큐
    bridge_weight = 0  # 현재 다리 위 무게
    
    while waiting:
        answer += 1
        bridge_weight -= crossing.popleft()
        
        if bridge_weight + waiting[0] <= weight:
            bridge_weight += waiting[0]
            crossing.append(waiting.popleft())
        else:
            crossing.append(0)
    
    answer += len(crossing)
    
    return answer