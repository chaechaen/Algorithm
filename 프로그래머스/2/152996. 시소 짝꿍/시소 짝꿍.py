from collections import Counter

def solution(weights):
    
    count = Counter(weights) # 키가 몸무게 값이 수
    ans = 0
    
    for w in count:
        
        # 두 사람의 몸무게가 완전히 같을 때 (1:1)
        if count[w] > 1: # 중복되는 몸무게가 2개 이상일 때
            ans += count[w] * (count[w] - 1) // 2 # 같은 몸무게 가진 사람끼리 짝을 짓는 경우의 수
            
        # 한 사람이 다른 사람의 3/2배일 때 (2:3)
        if w * 3/2 in count:
            ans += count[w] * count[w * 3/2]
            
        # 한 사람이 다른 사람의 2배일 때 (2:4)
        if w * 2 in count:
            ans += count[w] * count[w * 2]
            
        # 한 사람이 다른 사람의 4/3배일 때 (3:4)
        if w * 4/3 in count:
            ans += count[w] * count[w * 4/3]
    
    return ans