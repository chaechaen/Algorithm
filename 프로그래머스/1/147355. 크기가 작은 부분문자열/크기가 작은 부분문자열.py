def solution(t, p):
    length = len(p)
    
    lst = []
    for i in range(len(t)):
        sliced = t[i:i+length]
        if len(sliced) == length:
            lst.append(sliced)
    print(lst)
    cnt = 0
    for s in lst:
        if int(s) <= int(p):
            cnt += 1
    
    return cnt