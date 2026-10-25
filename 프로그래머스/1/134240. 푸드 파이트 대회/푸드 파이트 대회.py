from collections import deque

def solution(food):
    
    cnt = len(food) - 1
    dq = deque(['0'])
    for i in range(len(food) - 1, 0, -1):
            res = food[i] // 2
            if res != 0:
                dq.appendleft(str(cnt) * res)
                dq.append(str(cnt) * res)
                cnt -= 1
            else:
                cnt -= 1
            
    return ''.join(list(dq))