def solution(arr1, arr2):
    # 결과 행렬 크기: arr1의 행 * arr2의 열
    row_size = len(arr1)
    col_size = len(arr2[0])
    
    ans = [[0] * col_size for _ in range(row_size)]
    
    for r in range(row_size):
        for c in range(col_size):
            # r번째 가로줄과 c번째 세로줄을 타고 이동하며 곱함
            for k in range(len(arr1[0])):
                ans[r][c] += arr1[r][k] * arr2[k][c]
    
    return ans