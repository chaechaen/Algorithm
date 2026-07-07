def solution(numbers):
    
    res = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]: # 현재 숫자가 스택 젤 위 숫자보다 크면
            last_idx = stack.pop() # 가장 위 숫자를 꺼내고
            res[last_idx] = numbers[i] # 그 위치에 현재 숫자 넣기
        
        stack.append(i)
        
    return res