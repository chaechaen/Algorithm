def solution(elements):
    
    double_elements = elements + elements
    
    unique_sums = set() # 중복 제거
    
    for i in range(len(elements)):
        curr_sum = 0
        
        for j in range(len(elements)):
            curr_sum += double_elements[i + j]
            unique_sums.add(curr_sum)
    
    return len(unique_sums)