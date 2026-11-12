def solution(n, m, section):
    whole = [1] * n
    
    for i in section:
        whole[i-1] = 0
        
    ans = 0
    for i in range(len(whole)):
        if whole[i] == 0:
            whole[i:i+m] = [1] * m
            ans += 1
            
    return ans