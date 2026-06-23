def solution(video_len, pos, op_start, op_end, commands):
    
    def intFunc(time):
        return 60 * int(time.split(":")[0]) + int(time.split(":")[-1])
    
    def isBetweenOpn(op_start1, op_end1, pos1):
        if op_start1 <= pos1 <= op_end1: # 오프닝 사이에 있으면
            return op_end1
        else: return pos1
    
    def leftTime(pos1):
        if pos1 > video_len1: # 만약 남은 길이가 10초 미만이면
            return video_len1
        if pos1 < 0:
            return 0
        else: return pos1
    
    def transSec(pos1): 
        mm = pos1 // 60
        ss = pos1 % 60
        return f"{mm:02d}:{ss:02d}"
    
    video_len1 = intFunc(video_len) 
    pos1 = intFunc(pos)
    op_start1 = intFunc(op_start)
    op_end1 = intFunc(op_end)
    
        
    for i in commands:
        pos1 = isBetweenOpn(op_start1, op_end1, pos1) # 오프닝 구간 체크
        
        if i == "next":
            pos1 = pos1 + 10
        elif i == "prev":
            pos1 = pos1 - 10
            
        pos1 = leftTime(pos1) # 남은 시간 체크
        
        pos1 = isBetweenOpn(op_start1, op_end1, pos1) # 오프닝 구간 다시 체크
        
    return transSec(pos1)
        