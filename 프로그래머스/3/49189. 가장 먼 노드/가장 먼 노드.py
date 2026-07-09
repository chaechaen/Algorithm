import heapq

def solution(n, edge):
    
    def dijkstra(n, graph, start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        queue = []
        
        heapq.heappush(queue, (0, start))
        
        while queue:
            curr_dist, curr_node = heapq.heappop(queue)
            
            if dist[curr_node] < curr_dist:
                continue
            
            for next_node, weight in graph[curr_node]:
                cost = curr_dist + weight
                
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))
                    
        return dist
    
    graph = [[] for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        
    dist_table = dijkstra(n, graph, 1)
    
    max_node = max(dist_table[1:]) # 0번 인덱스 inf 제외
    return dist_table[1:].count(max_node)