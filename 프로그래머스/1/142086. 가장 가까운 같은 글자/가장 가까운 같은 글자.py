def solution(s):
    
    lst = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            idx = s[:i].rfind(s[i])
            lst.append(i - idx)
        else:
            lst.append(-1)
            
    return lst