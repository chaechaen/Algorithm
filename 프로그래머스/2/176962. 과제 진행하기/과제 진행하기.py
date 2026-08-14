def solution(plans):
    converted = []
    for name, start, time in plans:
        h, m = map(int, start.split(":"))
        start_min = h * 60 + m
        converted.append([name, start_min, int(time)])
    
    # 시작 시각 기준 오름차순 정렬
    converted.sort(key=lambda x: x[1])
    
    stack = []   # 멈춰둔 과제 [과제명, 남은시간]
    answer = []  # 끝낸 과제 순서
    
    # 다음 과제와 비교하며 하나씩 진행
    for i in range(len(converted) - 1):
        name, start, time = converted[i]
        next_start = converted[i+1][1] # 다음 과제 시작 시각
        
        finish_time = start + time # 현재 과제가 끝나는 시각
        
        # 끝나는 시각 > 새 과제 시작 시각 (다 못 끝냄)
        if finish_time > next_start:
            # stop하고 남은 시간 계산해서 스택에 저장
            rem_time = finish_time - next_start
            stack.append([name, rem_time])
            
        # 끝나는 시각 <= 새 과제 시작 시각 (완벽히 끝냄)
        else:
            answer.append(name) # 과제 완료
            
            # 남은 여유 시간 계산
            extra_time = next_start - finish_time
            
            # 여유 시간이 있고 멈춰둔 과제가 있다면, 스택에서 꺼내서 진행
            while extra_time > 0 and stack:
                # 가장 최근에 멈춘 과제
                st_name, st_rem_time = stack[-1]
                
                if st_rem_time <= extra_time:
                    # 멈춰둔 과제도 완벽히 끝낼 수 있음
                    extra_time -= st_rem_time
                    answer.append(stack.pop()[0]) # 완벽히 끝냈으니 stack.pop()
                else:
                    # 일부분만 진행하고 여유 시간 소진
                    stack[-1][1] -= extra_time
                    extra_time = 0
                    
    # 마지막 과제 처리 및 스택에 남은 과제들 털기
    answer.append(converted[-1][0]) # 정렬된 마지막 과제는 무조건 완료됨
    
    while stack:
        answer.append(stack.pop()[0]) # 최근에 멈춘 순서대로 pop
        
    return answer