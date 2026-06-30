def solution(numbers):
    
    cnt = 0
    ans = set()
    visited = [False] * len(numbers)
    
    # 소수 판별 함수
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def dfs(curr_num):
        
        # A. 정답 확인/업데이트
        if curr_num: # 빈 문자열이 아닐 때 소수 검사
            num = int(curr_num)
            if is_prime(num):
                ans.add(num)
            
        # B. 탈출/가지치기
        if len(curr_num) == len(numbers):
            return # back
        
        # C. 하위 노드로 파고들기
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                
                dfs(curr_num + numbers[i])
                visited[i] = False
            
    dfs("")
    return len(ans)