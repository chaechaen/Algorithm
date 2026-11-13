def solution(d, budget):
    d.sort()
    res = 0
    
    for i in d:
        if budget >= i:
            budget -= i
            res += 1
    
    return res