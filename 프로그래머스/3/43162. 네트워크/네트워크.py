def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for nxt_node in range(n):
            if computers[node][nxt_node] == 1 and not visited[nxt_node]:
                dfs(nxt_node)
                
    ans = 0            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
            
    return ans