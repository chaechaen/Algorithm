def solution(routes):
    
    routes.sort(key=lambda x: x[1])
    
    ans = 0
    end = -30001
    
    for s, e in routes:
        if s > end: # 폐구간이므로 같은 건 포함 x (경계에 있으면 단속 가능하므로)
            ans += 1
            end = e
            
    return ans