from collections import Counter

def solution(topping):
    right_cnt = Counter(topping) # 오른쪽 그룹의 토핑 정보
    
    left_set = set()
    
    res = 0
    
    for i in topping:
        left_set.add(i) # topping을 앞에서부터 하나씩 떼어다 왼쪽 그룹한테 줌
        
        right_cnt[i] -= 1 # 오른쪽 그룹에서 현재 토핑 개수를 1 감소시킴
        
        if right_cnt[i] == 0: # 아예 그 개수가 0이 되면
            del right_cnt[i] # 종류 자체를 삭제해줌
            
        if len(left_set) == len(right_cnt):
            res += 1
    
    return res