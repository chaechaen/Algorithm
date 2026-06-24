def solution(n, times):
    
    left = 1 # 걸릴 수 있는 최소 시간
    right = max(times) * n # 최대 시간
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        total_people = 0
        for time in times:
            total_people += mid // time # 각 심사관이 mid분 동안 처리 가능한 사람 수
            
        if total_people >= n: # mid분 안에 n명 심사 가능
            answer = mid # 정답 후보 저장
            right = mid - 1 # 시간 줄여보기
        else: # 시간 부족해서 n명 다 심사 못 함
            left = mid + 1 # 시간 더 줘야 함
            
    return answer