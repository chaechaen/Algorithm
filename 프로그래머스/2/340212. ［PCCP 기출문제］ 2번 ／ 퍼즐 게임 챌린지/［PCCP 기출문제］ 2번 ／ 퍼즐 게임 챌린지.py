def solution(diffs, times, limit):
    
    def get_total_time(level):
        total_time = 0
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1] if i > 0 else 0
            
            # 난이도가 내 레벨 이하인 경우 (안 틀림)
            if diff <= level:
                total_time += time_cur
            # 난이도가 내 레벨보다 높은 경우 (틀림)
            else:
                total_time += (diff - level) * (time_cur + time_prev) + time_cur
                
        return total_time
    
    # 이분 탐색
    left = 1 # 숙련도 최솟값
    right = max(diffs) # 숙련도 최댓값
    answer = right # 정답
    
    while (left <= right):
        mid = (left + right) // 2 # 중간 레벨 테스트
        
        if get_total_time(mid) <= limit: # mid 레벨로 풀었을 때 limit 이내인지 확인
            answer = mid # 일단 조건 만족하니까 정답 후보
            right = mid - 1 # 더 낮은 레벨도 되는지 확인
        else:
            left = mid + 1 # 레벨 높임
            
    return answer