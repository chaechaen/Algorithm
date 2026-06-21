def solution(citations):
    newlst = sorted(citations, reverse=True)
    
    for i, value in enumerate(newlst):
        if i + 1 > value:
            return i
    
    return len(citations)
    