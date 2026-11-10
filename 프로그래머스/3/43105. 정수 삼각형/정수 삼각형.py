def solution(triangle):
    # 맨 아랫줄 바로 윗줄부터 시작해서 0번째 줄까지 거꾸로 올라가며 누적합 구함
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 자기보다 아래 있는 줄의 양옆 숫자 중 더 큰 값 선택
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            
    return triangle[0][0]