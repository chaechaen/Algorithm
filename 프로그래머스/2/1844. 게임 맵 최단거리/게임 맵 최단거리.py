from collections import deque

def solution(maps):
    
    dr = [-1, 1, 0, 0] # 상하
    dc = [0, 0, -1, 1] # 좌우
    
    rows = len(maps) # 전체 행의 개수
    cols = len(maps[0]) # 전체 열의 개수
    
    visited = [[False] * cols for _ in range(rows)] # 방문표시 초기화
    
    queue = deque([(0, 0, 1)]) # 이동거리 포함 (시작 1)
    visited[0][0] = True
    
    while queue:
        r, c, ans = queue.popleft()
        
        if r == rows - 1 and c == cols - 1: # 목적지 도착 시 누적거리 리턴
            return ans
        
        for i in range(4): # 상하좌우 4방향
            nr = r + dr[i] # 다음 변화량
            nc = c + dc[i]
            
            if 0 <= nr < rows and 0 <= nc < cols: # 행렬 범위 벗어나지 않고
                if maps[nr][nc] == 1 and not visited[nr][nc]: # 갈 수 있는 곳이며 아직 미방문
                    queue.append((nr, nc, ans + 1)) # 거리 1 증가
                    visited[nr][nc] = True
                    
    return -1 # 목적지 미도착 시
                    