def solution(n):
    
    ans = 0 # 건전지 사용량
    
    while n > 0:
        # 홀수
        if n % 2 != 0:
            ans += 1 # 초반 1칸 점프 필수
            n -= 1
        # 짝수
        else:
            n //= 2
    return ans