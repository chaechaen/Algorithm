from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    lst = [i for i in range(1, n+1)]
    combination = list(combinations(lst, 5))
    
    for combi in combination:
        is_valid = True
        
        for i in range(len(q)):
            cnt = 0
            for num in q[i]: # q에 있는 각 시도의 하나의 요소에서
                if num in combi: # 만약 combi의 조합에 있는 숫자라면 count
                    cnt += 1
            
            if cnt != ans[i]: # 해당 인덱스에 대해 정답과 센 개수가 다르다면
                is_valid = False
                break
                
        if is_valid:
            answer += 1
            
    return answer