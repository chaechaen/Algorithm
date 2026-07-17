def solution(s):
    """
    1. 이진 변화 이전 값에서 0 다 없애고 그 길이를 파라미터로 보내서 이진법 함수 호출 -> 이진변환결과 받아와
    2. 그 결과에서 또 0 없애고 그 길이를 파라미터로 보내서 이진법 함수 호출 -> 이진변환결과 받아와
    3. 위 과정을 이진변환결과가 1이 될 때까지 계속 반복
    - 함수 호출 시마다 몇 회차인지 세고, 0 제외할 때마다 제외하는 0의 개수 세기 (누적)
    - 해당 회차와 제외한 0의 개수를 최종 반환
    """
    
    def make_binary(length):
        stack = []
        res = ''
        
        while length >= 1:
            remain = length % 2
            stack.append(remain)
            length //= 2
        
        for i in range(len(stack)):
            res += str(stack.pop())
        
        return res
    
    count_zero = 0
    rounds = 0
    
    while s != '1':
        count_zero += s.count('0')
        delete_zero = s.replace('0', '')
        length = len(delete_zero)
        rounds += 1
        s = make_binary(length)
    
    return [rounds, count_zero]