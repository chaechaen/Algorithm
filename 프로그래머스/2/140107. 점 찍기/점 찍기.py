def solution(k, d):
    
    '''
    원점과의 거리: i**2 + j**2 <= d**2
    y좌표의 최댓값: j <= 루트(d**2 - i**2)
    가능한 점의 개수: 0~최댓값 k 간격으로 몇 개 들어가는지 -> (최댓값 // k) + 1
    '''
    
    cnt = 0
    for i in range(0, d+1, k):
        max_y = int((d**2 - i**2) ** 0.5)
        
        cnt += (max_y // k) + 1
                
    return cnt