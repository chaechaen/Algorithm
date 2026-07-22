def solution(land):
    """
    두 번째 행부터 시작해서 위 행에서 같은 열을 제외한 칸들 중 가장 큰 값 더해주면서 내려오기
    """
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])
        
    return max(land[-1])