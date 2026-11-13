def solution(k, m, score):
    
    sr_score = sorted(score, reverse = True)
    
    add = 0
    lst = []
    for i in range(0, len(sr_score), m):
        if len(sr_score[i:i+m]) == m:
            lst.append(sr_score[i:i+m])
    
    for apple in lst:
        add += min(apple) * m
        
    return add