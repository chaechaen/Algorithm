def solution(n):
    
    # 스택에 나머지를 넣고 하나씩 for문 돌려 빼서 문자열 붙이기
    
    def make_binary(num):
    
        binary = ""
        stack = []

        while num >= 1:
            remain = num % 2
            stack.append(remain)
            num //= 2

        for i in range(len(stack)):
            binary = binary + str(stack.pop())
        
        return binary.count('1')
    
    # 반복 돌면서 찾기
    nxt = n + 1
    
    while True:
        if nxt > n:
            if make_binary(n) == make_binary(nxt):
                return nxt
            
        nxt += 1