def solution(n, lost, reserve):
    
    dic = {}
    for student in range(1, n+1):
        # 여벌이 있는데 도난 당함 -> 1개
        if student in lost and student in reserve:
            dic[student] = 1
        # 잃어버린 학생 -> 체육복은 0개
        elif student in lost:
            dic[student] = 0
        # 여벌 있는 학생 -> 2개
        elif student in reserve:
            dic[student] = 2
        # 걍 아무 일도 없는 학생 -> 1개
        else:
            dic[student] = 1
        
    for i in range(1, n+1):
        if dic[i] == 2: # value가 2인 학생 (여벌이 있다면)
            if i-1 in dic and dic[i-1] == 0: # 앞 학생이 존재하고 체육복이 없다면? 빌려줌
                dic[i] -= 1
                dic[i-1] += 1
            elif i+1 in dic and dic[i+1] == 0: # 뒤 학생도 체크해서 체육복 없으면 빌려줌
                dic[i] -= 1
                dic[i+1] += 1
                
    ans = 0
    for count in dic.values():
        if count >= 1:
            ans += 1
            
    return ans