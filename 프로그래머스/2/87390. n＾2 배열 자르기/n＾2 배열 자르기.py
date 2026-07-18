def solution(n, left, right):
    ans = []
    
    for i in range(left, right + 1):
        # 행렬에서 어느 위치에 있었는지 파악
        row = i // n
        col = i % n
        
        # 행과 열 중 더 큰 값에 1을 더하기
        ans.append(max(row, col) + 1)
        
    return ans