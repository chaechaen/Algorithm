def solution(s):
    
    def is_pair(new_s):
        lst = []
        
        pair = {')': '(', '}': '{', ']': '['}
        
        for i in new_s:
            if i in ('(', '{', '['): # 여는 괄호면
                lst.append(i) # 걍 넣기
            else: # 닫는 괄호면 짝 맞춰보기
                # 스택이 비어있거나 맨 위가 내 짝이 아니면
                if not lst or lst[-1] != pair[i]:
                    return False
                lst.pop() # 짝이 맞으면 제거
        
        return len(lst) == 0 # 스택이 비어있어야 함
    
    cnt = 0
    
    new_s = s
    for i in range(len(s)):
        if is_pair(new_s):
            cnt += 1
        new_s = new_s[1:] + new_s[0]
            
    return cnt