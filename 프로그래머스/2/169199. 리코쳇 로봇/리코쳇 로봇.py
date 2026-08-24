from collections import deque

def solution(board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    rows = len(board)
    cols = len(board[0])
    
    visited = [[False] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "R":
                start_r, start_c = (r, c)
            elif board[r][c] == "G":
                end_r, end_c = (r, c)
    
    
    # 시작 큐를 만들어
    queue = deque([(start_r, start_c, 0)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c, cost = queue.popleft()
        
        if r == end_r and c == end_c:
            return cost
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # while문으로 지금 이동했을 때 벽도 아니고 장애물도 아니라면 끝까지 이동해보도록
            while 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "D":
                nr += dr[i] # 한 칸 더 전진 (부딪힐 때까지 가보자)
                nc += dc[i]
                
            # 만약 부딪혀서 탈출하면
            nr -= dr[i]
            nc -= dc[i] # 한 칸씩 덜 가
            
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, cost + 1))
            
    return -1
            
            
            