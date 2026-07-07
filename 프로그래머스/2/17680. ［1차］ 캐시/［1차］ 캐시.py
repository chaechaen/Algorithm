from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5 # 캐시 크기가 0일 때 전부 miss
    
    queue = deque([])
    
    time = 0
    
    for i in cities:
        
        i = i.lower()
        
        # 큐에 없는데, 캐시 크기 초과하지 않은 경우 -> 걍 append, time+=5
        if i not in queue and len(queue) < cacheSize:
            queue.append(i)
            time += 5
        
        # 큐에 없는데, 캐시 크기를 초과한 경우 -> queue.popleft, append, time+=5
        elif i not in queue and len(queue) >= cacheSize:
            queue.popleft()
            queue.append(i)
            time += 5
        
        # 큐에 존재하는 경우 -> 걍 time+=1, 그리고 가장 최근 사용됐으니 젤 뒤로 이동시켜야 함.
        elif i in queue:
            time += 1
            queue.remove(i)
            queue.append(i)
        
    return time
            