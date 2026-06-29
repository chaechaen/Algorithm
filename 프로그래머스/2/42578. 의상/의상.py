def solution(clothes):
    
    dic = {}
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        
        if key not in dic:
            dic[key] = []
        dic[key].append(value)
        
    if len(dic) == 1: # 의상종류가 1개일 때
        for key in dic:
            return len(dic[key]) # 걍 그 종류의 의상 개수가 정답
    
    # 의상 종류가 여러 개일 때
    cnt = 0
    for key in dic:
        cnt += len(dic[key])
    
    total_combi = 1
    for key in dic:
        total_combi *= len(dic[key]) + 1 # 안 입는 경우도 +1
    
    return total_combi - 1 # 아예 암것도 안 입는 경우 -1