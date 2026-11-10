def solution(m, n, puddles):
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for x, y in puddles:
        dp[y][x] = -1 # 행렬이므로.
        
        
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 물에 잠긴 지역이거나 시작점이면 패스
            if dp[i][j] == -1 or (i == 1 and j == 1):
                continue
                
            # 위쪽에서 오는 경우
            from_top = dp[i-1][j] if dp[i-1][j] != -1 else 0
            
            # 왼쪽에서 오는 경우
            from_left = dp[i][j-1] if dp[i][j-1] != -1 else 0
            
            dp[i][j] = (from_top + from_left) % 1000000007
            
    return dp[n][m]
    