from itertools import combinations

def solution(nums):
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    combi = list(combinations(nums, 3))
    
    cnt = 0
    for c in combi:
        if is_prime(sum(c)):
            cnt += 1
            
    return cnt