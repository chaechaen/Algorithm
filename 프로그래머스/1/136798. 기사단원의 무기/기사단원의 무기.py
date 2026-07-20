def solution(number, limit, power):
    
    def factor(n):
        cnt = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                cnt += 1
                
                if i ** 2 != n:
                    cnt += 1
        return cnt # 약수 개수
    
    lst = []
    for i in range(1, number+1):
        result = factor(i)
        lst.append(result)
        
    for i in range(len(lst)):
        if lst[i] > limit:
            lst[i] = power
    
    return sum(lst)