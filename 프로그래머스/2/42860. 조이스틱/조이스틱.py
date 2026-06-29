def solution(name):
    # JEROEN ===> AAAAAA
    
    # 초기 설정은 글자수만큼의 A
    # 만약 A가 개많으면? -> -> -> .. 이것보다 걍 <- 이렇게 하는게 빠름
    # 즉, 연속된 A가 끝나는 지점을 생각해야 함. endA라고 한다면?
    
    total_move = 0
    len_name = len(name)
    
    # 좌우 이동의 최댓값은 걍 오른쪽으로 쭉 직진 했을 때의 횟수 (거꾸로 안 돌아오는 버전)
    cursor = len_name - 1
    
    for i in range(len_name):
        ch = name[i]
        # 위/아래 변경 횟수
        move_up = ord(ch) - ord('A')
        move_down = ord('Z') - ord(ch) + 1 # 왜 +1?
        total_move += min(move_up, move_down)
        
        # 좌우 이동 횟수
        next_i = i + 1 # A가 끝나는 지점까지 건너뛰기
        
        while next_i < len_name and name[next_i] == 'A':
            next_i += 1
            
        right_turn = i + i + (len_name - next_i) # 오른쪽으로 가다가 빽해서 왼쪽 끝으로 돌아가기
        left_turn = (len_name - next_i) + (len_name - next_i) + i # 처음부터 왼쪽으로 먼저 갔다가, 다시 빽해서 오른쪽으로 오기
        
        cursor = min(cursor, right_turn, left_turn)
        
    return total_move + cursor