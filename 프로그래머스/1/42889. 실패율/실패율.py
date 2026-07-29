from collections import Counter

def solution(N, stages):
    """
    - 실패율 = 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
    - 스테이지에 도달한 플레이어 수 = 현재 스테이지 번호 이상(>= i)인 플레이어 수의 합
    - 클리어하지 못한 플레이어 수 = 현재 스테이지 번호(i)에 멈춰있는 플레이어 수
    """
    
    cnt = Counter(stages)
    lst = []
    pass_stage = 0
    
    for i in range(1, N+1):
        not_cleared = cnt[i] # 클리어하지 못한 플레이어수 
        pass_stage = sum(cnt[key] for key in cnt if key >= i) # 스테이지에 도달한 플레이어수
        
        if pass_stage == 0: # 도달한 유저가 없는 경우
            rate = 0
        else:
            rate = not_cleared / pass_stage
        
        lst.append((i, rate))
        
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    
    res = [x[0] for x in sorted_lst]
    print(res)
    
    return res