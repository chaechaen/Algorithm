from collections import deque

def solution(prices):
    res = []
    queue = deque(prices)
    
    while queue:
        curr_price = queue.popleft()
        sec = 0
        
        for nxt_price in queue:
            sec += 1
            
            if curr_price > nxt_price: # 가격 떨어진 경우
                break
                
        res.append(sec)
        
    return res