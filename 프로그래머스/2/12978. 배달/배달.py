import heapq

def solution(N, road, K):
    
    # 다익스트라 알고리즘
    def dijkstra(n, graph, start):
        dist = [float('inf')] * (n + 1) # 최단거리 테이블

        dist[start] = 0 # 시작 노드(1번 마을) 초기화
        queue = []

        heapq.heappush(queue, (0, start)) # 큐에다가 (거리, 노드번호) 형태로 삽입

        while queue:
            curr_dist, curr_node = heapq.heappop(queue) # 최소 노드 꺼내서 각각에 넣어줌

            if dist[curr_node] < curr_dist: # 이미 최단거리가 있으면 패스
                continue

            for next_node, weight in graph[curr_node]:
                cost = curr_dist + weight

                if cost < dist[next_node]: # 거쳐서 가는게 기존보다 더 저렴하다면 갱신
                    dist[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))

        return dist
    
    # 그래프로 변환
    graph = [[] for _ in range(N+1)] # 노드 개수만큼 빈 리스트 만들기
    
    for a, b, c in road:
        graph[a].append((b, c)) # a번에 b로가는 거리 c 추가
        graph[b].append((a, c)) # 양방향이니까 b에 a로 가는 거리 c도 추가
        
    # 다익스트라 수행 (1번 마을부터)    
    dist_table = dijkstra(N, graph, 1)
    
    # K 시간 이하로 배달 가능한 마을 개수 세기
    res = 0
    for i in range(1, N+1):
        if dist_table[i] <= K:
            res += 1
            
    return res