def solution(n, t, m, p):
    """
    1. 0부터 숫자를 1씩 늘려가면서 n진수로 변환한 수를 계속 이어붙이기 (길이가 t*m 넘길 때까지)
    2. 완성된 문자열에서 p-1번 인덱스부터 m의 간격으로 t개 문자를 추출
    """

    DIGITS = "0123456789ABCDEF"
    
    def base_conversion(num):
        if num == 0:
            return "0"
        
        str_num = ""
        
        while num >= 1:
            num, r = divmod(num, n)
            str_num += DIGITS[r]
            
        return str_num[::-1]
    
    num = 0
    game_string = ""
    while len(game_string) < t * m:
        game_string += base_conversion(num)
        num += 1
        
    return game_string[p-1::m][:t] # p-1부터 m씩 건너뛰며 t개 가져옴