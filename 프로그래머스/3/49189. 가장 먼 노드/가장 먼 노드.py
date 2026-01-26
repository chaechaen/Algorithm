from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    # 인접리스트 만들기
    for e in edge: 
        # 양방향 그래프
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    def bfs(s, graph):
        max_dist = -1
        count = 0
        
        # 시작 노드 예약
        queue = deque()
        queue.append((s, 0))
        visited[s] = True
        
        while queue:
            # 방문
            cur, dist = queue.popleft() # 현재 노드
            
            if max_dist == dist:
                count += 1
            if max_dist < dist:
                max_dist = dist
                count = 1
                
            # (다음 노드) 예약
            for nxt in graph[cur]:
                if not visited[nxt]:
                    queue.append((nxt, dist+1))
                    visited[nxt] = True
        
        return count
                
    return bfs(1, graph) # 1번에서 시작