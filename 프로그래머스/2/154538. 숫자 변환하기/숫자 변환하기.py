from collections import deque

def solution(x, y, n):
    
    def bfs(graph, start, visited):
        queue = deque([start])
        
        visited[start] = 1 # 연산 횟수 기준점 1 적고 시작
    
        while queue:
            v = queue.popleft()
            
            if v == y: # 방금 꺼낸 숫자가 목적지라면
                return visited[v] - 1 # 기록판에 적힌 숫자에서 처음에 더했던 기준점 1을 빼고 정답
            
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = visited[v] + 1 # 연산 횟수 +1
                    
        return -1
    
    # 만약 시작부터 x==y라면 걍 바로 0 리턴
    if x == y:
        return 0
    
    # graph 만들기
    graph = [[] for _ in range(y + 1)]
    
    for curr in range(x, y+1):
        for next_num in (curr+n, curr*2, curr*3):
            if next_num <= y: # 다음 숫자가 목적지를 넘지 않을 때만
                graph[curr].append(next_num) # 길 연결
                
    visited = [0] * (y + 1) # 연산 횟수 기록판
    
    return bfs(graph, x, visited)