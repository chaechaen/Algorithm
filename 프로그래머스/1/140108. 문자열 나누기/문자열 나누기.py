def solution(s):
    res = 0
    i = 0
    
    while i < len(s):
        x = s[i]
        same_count = 0
        diff_count = 0
        
        for j in range(i, len(s)):
            if s[j] == x:
                same_count += 1
            else:
                diff_count += 1
            
            # 두 횟수가 같아지면 멈춤
            if same_count == diff_count:
                break
                
        # 분해 개수 증가
        res += 1
        # 다음 탐색 시작 위치를 j 다음으로 이동
        i = j + 1
        
    return res