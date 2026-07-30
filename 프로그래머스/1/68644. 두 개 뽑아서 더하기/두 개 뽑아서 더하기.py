from itertools import combinations

def solution(numbers):
    combi = list(combinations(numbers, 2))
    
    res = set()
    for c in combi:
        res.add(sum(c))
    
    ans = sorted(list(res))
    return ans