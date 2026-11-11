from itertools import combinations

def solution(number):
    res = list(combinations(number, 3))
    
    cnt = 0
    for i in res:
        if sum(i) == 0:
            cnt += 1
    
    return cnt