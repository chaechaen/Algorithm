def solution(k, dungeons):
    
    '''
    k = 현재 피로도
    dungeons = [최소 필요 피로도, 소모 피로도]
    유저가 탐험할 수 있는 최대 던전 수
    남은피로도=현재피로도-소모피로도
    남은피로도 >= 최소피로도 <- 이래야 계속 탐험 가능.
    '''
    
    # 각 던전을 이미 방문했는지 체크할 리스트
    visited = [False] * len(dungeons)
    
    # 최대 탐험 횟수
    max_cnt = 0
    
    def dfs(curr_k, cnt): # 현재 남은 피로도, 현재까지 들어간 던전 수
        nonlocal max_cnt
        max_cnt = max(max_cnt, cnt)
        
        for i in range(len(dungeons)):
            # 아직 방문 안 했고, 남은 피로도가 최소 피로도 이상?
            if visited[i] == False and curr_k >= dungeons[i][0]:
                visited[i] = True # 방문했음.
                
                dfs(curr_k - dungeons[i][1], cnt + 1) # 이제 소모피로도 만큼 깎고, cnt+1
                visited[i] = False # 다시 돌아왔을 때 방문 취소 -> 그래야 다시 조합 가능

    dfs(k, 0) # 첫 시작은 원래 피로도 k, 탐험 횟수 0
    
    return max_cnt