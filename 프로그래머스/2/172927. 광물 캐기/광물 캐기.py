def solution(picks, minerals):
    
    max_pick = sum(picks) * 5
    new_minerals = minerals[:max_pick] # 사용 가능한 최대 광물 수 만큼만
    
    groups = [new_minerals[i:i+5] for i in range(0, len(new_minerals), 5)] # 5개씩 그룹화
    
    cnt = []
    for g in groups:
        dia = g.count("diamond")
        iron = g.count("iron")
        stone = g.count("stone")
        cnt.append((dia, iron, stone)) # 각 그룹별 광물 개수 카운트
        
    cnt.sort(key=lambda x: (x[0], x[1], x[2]), reverse = True) # 가치 높은 순 정렬
    
    ans = 0
    dia_pick, iron_pick, stone_pick = picks
    
    for d, i, s in cnt:
        if dia_pick > 0:
            ans += d + i + s
            dia_pick -= 1
        elif iron_pick > 0:
            ans += d * 5 + i + s
            iron_pick -= 1
        elif stone_pick > 0:
            ans += d * 25 + i * 5 + s
            stone_pick -= 1
        else:
            break
            
    return ans