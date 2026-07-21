import math
from functools import reduce

def solution(arrayA, arrayB):
    # 철수의 최대공약수이면서 영희의 약수가 아니거나, 영희의 최대공약수이면서 철수의 약수가 아닌 수 중 가장 큰 양의 정수
    
    gcd_a = reduce(math.gcd, arrayA)
    gcd_b = reduce(math.gcd, arrayB)
    
    result = 0
    
    if gcd_a > 1:
        if all (b % gcd_a != 0 for b in arrayB):
            result = max(result, gcd_a)
            
    if gcd_b > 1:
        if all (a % gcd_b != 0 for a in arrayA):
            result = max(result, gcd_b)
                
    return result