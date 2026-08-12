def solution(babbling):
    
    can = ["aya", "ye", "woo", "ma"]
    seq = ["ayaaya", "yeye", "woowoo", "mama"]
    cnt = 0
    
    for b in babbling:        
        if any(s in b for s in seq): # 연속 발음이 단어 안에 하나라도 있으면
            continue
        
        for c in can:
            b = b.replace(c, " ") # 가능한 발음을 공백으로 치환
            
        if b.replace(" ", "") == "": # 공백 다 지웠을 때 빈 문자열만 남으면
            cnt += 1
            
    return cnt