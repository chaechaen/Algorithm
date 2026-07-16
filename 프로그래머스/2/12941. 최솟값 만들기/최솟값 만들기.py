def solution(A,B):
    
    sorted_A = sorted(A)
    sorted_B = sorted(B, reverse=True)
    
    res = 0
    for i in range(len(A)):
        res += sorted_A[i] * sorted_B[i]
    
    return res