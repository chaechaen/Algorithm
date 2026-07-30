from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    
    for c in course:
        menu_lst = []
        for order in orders:
            sorted_order = sorted(order)
        
            # 각 orders의 요소에서 나올 수 있는 course 조합
            menu_lst.extend(combinations(sorted_order, c))
            
        cnt = Counter(menu_lst) # 들어온 모든 c개짜리 조합의 개수를 센 딕셔너리 생성
        
        if cnt:
            max_val = max(cnt.values()) # 조합 개수가 가장 큰 걸 찾고
            if max_val >= 2: # 최소 2명 이상 주문 조건인지 확인
                for k, v in cnt.items():
                    if v == max_val:
                        ans.append("".join(k))
                        
    return sorted(ans)