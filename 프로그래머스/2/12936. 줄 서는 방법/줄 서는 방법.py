import math

def solution(n, k):
    """
    - 0-based 인덱스 처리를 위해 k에서 1을 먼저 뺌 (k -= 1)
    - 남아있는 사람 수(len(people) - 1)! 값으로 k를 나눠 현재 자리에 올 사람의 인덱스(idx = k // fact) 구하기
    - 해당 인덱스의 사람을 res에 추가하고 people에서 제거
    - k를 나머지(k %= fact)로 갱신하면서 남아있는 숫자가 없을 때까지 반복
    """
    
    people = [i for i in range(1, n + 1)]
    
    res = []
    k -= 1
    
    while people:
        fact = math.factorial(len(people) - 1) # 남은 사람 수의 팩토리얼
                             
        idx = k // fact # 현재 자리에 올 인덱스
        
        res.append(people.pop(idx)) # 해당 인덱스 값을 res에 추가, people에서 삭제
        
        k %= fact # k를 나머지 값으로 갱신
        
    return res
        
        
        