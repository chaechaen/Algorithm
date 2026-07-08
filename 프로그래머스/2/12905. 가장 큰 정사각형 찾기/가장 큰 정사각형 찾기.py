def solution(board):
    '''
    - 이걸 행렬로 본다면, (i,j)를 정사각형의 오른쪽 아래 꼭짓점이라고 생각했을 때
    - 바로 위는 (i-1, j), 바로 왼쪽은 (i, j-1), 왼쪽 대각선 위는 (i-1, j-1)
    '''
    
    row_len = len(board)
    col_len = len(board[0])
    
    max_side = 0
    
    # 첫 번째 행이나 첫 번째 열만 있는 경우, 1이 하나라도 있으면 최댓값은 1
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] == 1:
                max_side = 1

    # (1, 1)부터 시작해서 주변 3칸 검사
    for i in range(1, row_len):
        for j in range(1, col_len):
            # 현재 칸이 1일 때만 정사각형 확장 가능
            if board[i][j] == 1:
                # 위, 왼쪽, 대각선 위 중 최솟값을 찾고 1을 더하기
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                
                # 기록된 한 변의 길이 중 가장 큰 값 갱신
                if board[i][j] > max_side:
                    max_side = board[i][j]

    return max_side * max_side