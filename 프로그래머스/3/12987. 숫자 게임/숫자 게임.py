def solution(A, B):
    A.sort()
    B.sort()
    
    idx = 0
    res = 0
    for i in B:
        if i > A[idx]:
            res += 1
            idx += 1
            continue
        else:
            continue
            
    return res