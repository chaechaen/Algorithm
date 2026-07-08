def solution(n):
    '''
    n=1: 1개 / n=2: 2개 / n=3: 3개 / n=4: 5개 / n=5: 8개 ...
    '''
    
    if n <= 2:
        return n
    
    dp = [0, 1, 2] + [0] * (n-2)
    print(dp)
    
    for i in range(1, n-1):
        dp[i+2] = (dp[i]+dp[i+1]) % 1000000007
    
    return dp[-1]