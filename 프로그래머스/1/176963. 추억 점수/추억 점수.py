def solution(name, yearning, photo):
    
    dic = dict(zip(name, yearning))
    res = []
    
    print(dic)
    
    for i in photo:
        add = 0
        for n in i:
            if n in name:
                add += dic[n]
            else:
                continue
        res.append(add)
        
    return res