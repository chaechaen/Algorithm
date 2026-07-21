def solution(n):
    """
    - 0 없는 3진법 -> 3으로 나누었을 때의 나머지로 바꾸기
    - 나머지 0 처리 -> 원래 몫에서 1 빼주기
    - 3으로 나눈 나머지 계속 앞쪽에 붙여나가기
    """
    
    num_map = ['4', '1', '2']  # 나머지가 0, 1, 2 일 때 대응하는 문자
    answer = ''
    
    while n > 0:
        remainder = n % 3
        answer = num_map[remainder] + answer
        
        # 나머지가 0이면 n에서 1을 뺀 후 3으로 나눔
        if remainder == 0:
            n = (n - 1) // 3
        else:
            n = n // 3
            
    return answer