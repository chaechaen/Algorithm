def solution(numbers, target):
    answer = 0
    n = len(numbers) # 총 사용할 수 있는 숫자 개수
    
    def dfs(idx, current_sum):
        nonlocal answer
        
        if idx == n: # 탈출 조건 (숫자 끝에 도달했을 떄 종료)
            if current_sum == target:
                answer += 1
            return
        
        dfs(idx + 1, current_sum + numbers[idx]) # 현재 숫자를 더해서 다음 숫자로 넘어가기
        dfs(idx + 1, current_sum - numbers[idx]) # 현재 숫자를 빼서 다음 숫자로 넘어가기
        
    dfs(0,0) # 0번째부터 시작
    
    return answer