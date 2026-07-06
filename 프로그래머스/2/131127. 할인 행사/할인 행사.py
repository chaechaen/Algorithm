from collections import Counter

def solution(want, number, discount):
    '''
    - discount를 첫날부터 (전체 길이 - 10)날까지 순회
    - 현재 날짜부터 10일간의 할인 품목을 슬라이싱([i:i+10])해 Counter로 개수를 세기
    - 10일간의 할인 수량이 내가 원하는 수량을 모두 충족하는지 비교
    '''
    
    want_dic = {}
    for w, n in zip(want, number):
        want_dic[w] = n # 제품과 수량을 딕셔너리로
        
    
    counts = Counter(discount)
    print(counts)
    
    res = 0
    for i in range(len(discount) - 10 + 1):
        
        curr_10_days = Counter(discount[i:i+10]) # i번째부터 10일간의 할인 품목만 잘라
        
        is_match = True
        for key in want_dic:
            if curr_10_days[key] < want_dic[key]: # 원하는 수량보다 할인 수량이 적으면 X
                is_match = False
                break
        if is_match:
            res += 1
    
    return res