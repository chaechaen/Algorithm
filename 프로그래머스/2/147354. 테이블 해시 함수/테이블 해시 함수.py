def solution(data, col, row_begin, row_end):
    
    sorted_data = sorted(data, key = lambda x: (x[col-1], -x[0]))
    
    res = []
    
    for i in range(row_begin, row_end + 1):
        sum_res = 0 # 각 행마다 0부터 계산
        for j in sorted_data[i-1]:
            sum_res += j % i
        res.append(sum_res)
            
    ans = 0      
    for n in res:
        ans ^= n
    
    return ans