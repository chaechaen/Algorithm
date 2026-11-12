def solution(left, right):
    # 약수의 개수 구하기
    def count_divisor(num):
        cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
        return cnt
    
    res = 0
    for num in range(left, right+1):
        if count_divisor(num) % 2 == 0:
            res += num
            
        else:
            res -= num
            
    return res