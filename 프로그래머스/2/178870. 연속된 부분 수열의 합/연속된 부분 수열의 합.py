def solution(sequence, k):
    '''
    1. 가장 짧아야 할 것
    2. 길이가 같다면 앞에 나와야 할 것
    앞에 포인터 하나 a, 뒤에 포인터 하나 b
    '''
    
    a = 0
    b = 0
    
    curr_sum = sequence[0]
    
    min_length = float('inf')
    ans = []
    
    while b < len(sequence):
        if curr_sum == k:
            maybe = b - a + 1 # 현재 수열의 길이
            
            if maybe < min_length: # 기존에 찾은 것보다 더 짧으면 정답 후보 업뎃
                min_length = maybe
                ans = [a, b]
                
            curr_sum -= sequence[a] # 합에서 맨 앞 값을 빼고
            a += 1 # 한 칸 오른쪽으로 옮김
            
        elif curr_sum < k: # 합이 k보다 작을 때 -> 구간을 오른쪽으로 늘림
            b += 1
            if b < len(sequence): # 인덱스 범위 벗어나지 않을 때만
                curr_sum += sequence[b] # 한 칸 늘려 기존 합에 새로 추가
            
        else: # 합이 k보다 클 때 -> 구간을 왼쪽에서 줄임
            curr_sum -= sequence[a]
            a += 1
    
    return ans