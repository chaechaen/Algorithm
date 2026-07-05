import math

def solution(progresses, speeds):
    
    lst = []
    for i in range(len(progresses)):
        left_progress = 100 - progresses[i]
        x = math.ceil(left_progress/speeds[i]) # 배포되는 데 며칠이 필요하냐
        lst.append(x)
    
    res = []
    cnt = []
    for day in lst:
        if cnt and day > cnt[0]: # 스택이 비어있지 않으면서 현재 기능이 기존 기능보다 오래 걸릴 때
            res.append(len(cnt)) # 앞에 쌓인 기능들을 먼저 배포
            cnt = []
            
        cnt.append(day) # 현재 기능을 스택에 넣고
        
    if cnt: # 남아있는 기능들도 다 배포
        res.append(len(cnt))
    
    return res