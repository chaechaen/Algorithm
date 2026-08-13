def solution(keymap, targets):
    
    # 각 알파벳 만드는 데 필요한 버튼 클릭 횟수 저장하는 딕셔너리
    dic = {}
    
    for k in keymap:
        for i in range(len(k)):
            if k[i] not in dic:
                dic[k[i]] = i + 1
            else: # 이미 딕셔너리에 저장되어 있다면, 최솟값을 저장
                if dic[k[i]] > i + 1: # 현재값이 더 작다면 현재값을 저장
                    dic[k[i]] = i + 1
                else:
                    continue
    
    res = []
    
    for t in targets:
        cnt = 0
        
        for s in t:
            # 만약 targets에 있는 문자가 자판에 없으면
            if s not in dic:
                cnt = -1
                break
            else:
                cnt += dic[s]
        
        if cnt == -1:
            res.append(-1)
        else:
            res.append(cnt)
    
    return res