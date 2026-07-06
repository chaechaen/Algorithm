from collections import Counter

def solution(k, tangerine):
    '''
    - 내림차순 sort
    - 앞에서부터 하나씩 개수만큼 k에서 빼면서 확인
    '''
    
    cnt = Counter(tangerine)
    sorted_cnt = sorted(cnt.values(), reverse=True) # 개수(값)만 뽑아서 많은 순서대로 정렬
    res = 0 # 정답(종류 개수)
    
    for i in sorted_cnt:
        k -= i # k개에서 개수 줄임
        res += 1 # 종류 1개 추가
        
        if k <= 0: # k개를 모두 담았으면
            break
            
    return res