def solution(order):
    
    stack = []
    cnt = 0
    
    for box in range(1, len(order) + 1):
        stack.append(box)
        
        while stack and stack[-1] == order[cnt]:
            stack.pop()
            cnt += 1

    return cnt