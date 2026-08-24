from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    target = (sum1 + sum2) // 2
    
    cnt = 0
    max_cnt = len(queue1) * 4 # 무한루프 방지용
    
    while (sum1 != target):
        
        if cnt > max_cnt:
            return -1
        
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num

        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
            
        cnt += 1
        
    return cnt
        
    
    