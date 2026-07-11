def solution(n):
    """
    1부터 n까지 투포인터로 범위 움직이면서 합을 만들어내기
    """
    
    a = 0
    b = 0
    
    numbers = [_ for _ in range(1, n+1)]
    
    curr_sum = numbers[0]
    
    min_len = float('inf')
    cnt = 0
    
    while b < len(numbers):
        if curr_sum == n:
            cnt += 1
            
            curr_sum -= numbers[a]
            a += 1
            
        elif curr_sum < n:
            b += 1
            if b < len(numbers):
                curr_sum += numbers[b]
            
        else:
            curr_sum -= numbers[a]
            a += 1
    
    return cnt