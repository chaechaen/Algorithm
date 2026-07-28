def solution(n, k):
    """
    몫을 q, 나머지를 r이라고 한다면 q, r = divmod(n, k)
    그리고 그 다음에 n자리에 들어갈 녀석은 q가 되어야 함
    몫이 1이 될 때까지 구해 그 나머지를 거꾸로 이어붙이기
    
    진법 변환 이후 0을 기준으로 split해서 소수 판별하고 소수인 요소를 새로운 리스트에 넣어 개수 세기
    """
    
    # 진법 변환 함수
    def base_conversion(n, k):
        num_str = ""
        
        while n >= 1:
            q, r = divmod(n, k)
            n = q
            num_str = num_str + str(r)

        return num_str[::-1]
    
    # 소수 판별 함수
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    string = base_conversion(n, k)
    
    # 0을 기준으로 자르기 (split은 그 자체로 리스트)
    candidates = string.split('0')
    
    res = []
    for x in candidates:
        if x: # x가 빈 문자열이 아닐 때
            if is_prime(int(x)):
                res.append(x)
    
    return len(res)
    