def solution(board, h, w):
    
    n = len(board)
    
    count = 0 # 같은 색으로 색칠된 칸의 개수 저장
    
    # 상하좌우
    dh = [1, -1, 0, 0] # 상하
    dw = [0, 0, -1, 1] # 좌우
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count
    