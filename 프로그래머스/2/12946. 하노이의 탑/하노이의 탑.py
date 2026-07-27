def solution(n):
    """
    1. 위쪽에 있는 n-1개 원판 2번으로 치우기
    2. 가장 큰 원판 3번으로 치우기
    3. 치워둔 n-1개 원판 3번으로 가져오기
    """
    
    answer = []
    
    def hanoi(cnt, start, end, via):
        if cnt == 1: # 원판이 1개인 경우 걍 목적지로 옮기고 종료
            answer.append([start, end])
            return
        
        hanoi(cnt - 1, start, via, end) # 1번 과정 (1번에서 3번을 거쳐 2번으로 치우기)
        answer.append([start, end]) # 2번 과정 (맨 밑 가장 큰 원판을 1번에서 3번으로 이동)
        hanoi(cnt - 1, via, end, start) # 3번 과정 (치워둔 2번에서 1번을 거쳐 3번으로 가져오기)
        
    hanoi(n, 1, 3, 2)
    
    return answer