import heapq

def solution(n, k, enemy):
    
    queue = []
    
    for i in range(len(enemy)):
        heapq.heappush(queue, enemy[i])
        
        if len(queue) > k: # 힙에 들어간 적의 수가 무적권 개수 넘기면
            n -= heapq.heappop(queue) # 작은 적을 내 병사로 막기
            
        if n < 0:
            return i
        
    return len(enemy) # 끝까지 방어에 성공한 경우