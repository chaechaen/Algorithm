from collections import deque

def solution(n, wires):
    
    def bfs(start, graph, n):
        visited = [False] * (n + 1) # 1~n이므로
        queue = deque([start])
        visited[start] = True
        cnt = 1
        
        while queue:
            x = queue.popleft()
            
            for i in graph[x]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    cnt += 1
                    
        return cnt
                    
    ans = n
    
    for i in range(len(wires)):
        # i번째 간선을 제외한 나머지로 그래프 만들기
        graph = [[] for _ in range(n + 1)]
        
        for j, (u, v) in enumerate(wires):
            if i == j:
                continue # 이번 간선 끊기
            graph[u].append(v)
            graph[v].append(u)
            
        cnt = bfs(1, graph, n)
        
        diff = abs(cnt - (n - cnt))
        ans = min(ans, diff)
        
    return ans