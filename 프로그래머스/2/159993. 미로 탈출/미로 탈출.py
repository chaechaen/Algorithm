from collections import deque

def solution(maps):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    rows = len(maps)
    cols = len(maps[0])
    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                exit = (r, c)
                
    def bfs(start_pos, target_pos):
        visited = [[False] * cols for _ in range(rows)]
        
        start_r, start_c = start_pos
        target_r, target_c = target_pos
        
        queue = deque([(start_r, start_c, 0)]) # r, c, 이동시간
        visited[start_r][start_c] = True
        
        while queue:
            r, c, cost = queue.popleft()
            
            if r == target_r and c == target_c:
                return cost
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        queue.append((nr, nc, cost + 1))
                        visited[nr][nc] = True
                        
        return -1 # 목표 도달 x
    
    # S -> L 최단거리
    time1 = bfs(start, lever)
    if time1 == -1:
        return -1
    
    # L -> E 최단거리
    time2 = bfs(lever, exit)
    if time2 == -1:
        return -1
    
    return time1 + time2