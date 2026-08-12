def solution(numbers):
    """
    1) numbers를 순회하면서 그 요소(x) 원본을 먼저 저장 => org
    2) x += 1을 해서 그 수에 대해 1씩 늘려가면서 org랑 계속 비교해서 숫자 몇 개 다른지.
        - 참고로 몇 개 다른지 세려면, XOR연산(다르면 1)을 해서 1의 개수를 세면 됨.
    3) 1의 개수가 1~2개인 순간 stop
    """
    
    res = []
    
    for x in numbers:
        org = x
        
        while True:
            # 짝수면 +1, 홀수면 가장 오른쪽 0이 있는 비트 자릿수만큼 한 번에 점프
            if x % 2 == 0:
                x += 1
            
            # 가장 오른쪽 0 비트를 찾아 1로 바꾸는 가산값 계산
            else:
                x += (~x & (x + 1)) // 2
            
            cnt = (x ^ org).bit_count() # 몇 개 다른지 XOR 연산으로 세기
        
            if 1 <= cnt <= 2:
                res.append(x)
                break
            
    return res