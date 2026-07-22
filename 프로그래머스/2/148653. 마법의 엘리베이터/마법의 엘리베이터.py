def solution(storey):
    """
    1. 숫자가 < 5 인 경우: 내리는 게 유리 -> 숫자 만큼 소모
    2. 숫자가 > 5 인 경우: 올리는 게 유리 -> 10-숫자 만큼 소모 + 다음 자릿수 +1
    3. 숫자가 == 5 인 경우: 다음 숫자가 5 이상이면 올림, 다음 숫자가 5 미만이면 내림
    """
    
    cnt = 0
    
    while storey > 0:
        remainder = storey % 10 # 일의 자리

        if remainder < 5: # 현재 자릿수가 5 미만이면 내림
            cnt += remainder
        elif remainder > 5: # 현재 자릿수가 5 초과면 올림
            cnt += (10 - remainder)
            storey += 10 # 다음 자릿수 +1
        else: # 현재 자릿수가 5면
            nxt = (storey // 10) % 10 # 다음 자릿수 확인
            if nxt >= 5: # 다음 자릿수가 5 이상이면 올림 해두기
                cnt += (10 - remainder)
                storey += 10
            else: # 다음 자릿수가 5 미만이면 내림
                cnt += remainder
                
        storey //= 10 # 다음 자릿수로 이동
        
    return cnt
        