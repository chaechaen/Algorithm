def solution(x, n):
    ans = []
    num = x
    while len(ans) < n:
        
        ans.append(num)
        num += x
        
    return ans