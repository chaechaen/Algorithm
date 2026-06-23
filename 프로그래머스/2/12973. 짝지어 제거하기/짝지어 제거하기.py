def solution(s):
    newLst = []
    lst = list(s)
    
    for i in lst:
        newLst.append(i)
        if len(newLst) < 2:
            continue
        else:
            if newLst[-1] == newLst[-2]:
                newLst.pop()
                newLst.pop()
            else:
                continue
                
    if len(newLst) == 0:
        return 1
    else:
        return 0
            
    
    