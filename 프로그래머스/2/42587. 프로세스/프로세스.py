def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    res = 0
    
    while queue:
        cur = queue.pop(0) # 하나 꺼내기
        
        if any(cur[1] < item[1] for item in queue): # 현재 꺼낸 것보다 더 우선순위 높은 게 있는지
            queue.append(cur) # 있다면 맨 뒤에 넣기
        else:
            res += 1
            if cur[0] == location:
                return res