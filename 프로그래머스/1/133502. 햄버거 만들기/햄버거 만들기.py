def solution(ingredient):
    
    hamburger = [1, 2, 3, 1]
    
    stack = []
    cnt = 0
    
    for i in ingredient:
        stack.append(i)
        
        if stack and stack[-4:] == hamburger:
            cnt += 1
            del stack[-4:]
            
    return cnt