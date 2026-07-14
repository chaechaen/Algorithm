def solution(n):
    dp = [0] * (n+1)
    
    dp[0] = 0
    dp[1] = 1
    
    for i in range(n-1):
        dp[i+2] = dp[i] + dp[i+1]
    
    return dp[i+2] % 1234567