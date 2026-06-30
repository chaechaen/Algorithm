def solution(word):
    
    vowels = "AEIOU"
    cnt = 0

    def dfs(curr_word): 
        nonlocal cnt
        
        # 탈출 조건 (정답 찾음)
        if curr_word == word:
            return True
        
        # 만약 길이 제한에 도달하면? 백트래킹. 직전 갈림길로 돌아가.
        if len(curr_word) == 5:
            return False
        
        # 하위 노드로 파고들기
        for i in range(5):
            nxt_word = curr_word + vowels[i]
            cnt += 1
            
            if dfs(nxt_word) == True:
                return True
            
        return False

    dfs("") # 첫 시작
    
    return cnt