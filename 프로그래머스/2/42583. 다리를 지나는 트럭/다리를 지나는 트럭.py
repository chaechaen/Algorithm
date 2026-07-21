from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    time = 0
    curr_weight = 0
    
    while bridge:
        time += 1
        leaving = bridge.popleft()
        curr_weight -= leaving
        
        if trucks:
            if curr_weight + trucks[0] <= weight: # 다음 트럭까지 합쳐도 가능한지 확인
                truck = trucks.popleft()
                bridge.append(truck) # 가능하면 트럭을 다리에 올림
                curr_weight += truck
            
            else:
                bridge.append(0) # 올라가지 못하면 빈 공간 넣기
    
    return time