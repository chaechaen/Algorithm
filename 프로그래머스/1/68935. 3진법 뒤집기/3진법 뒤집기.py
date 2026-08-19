def solution(n):
    def base_conversion(n):
        s = ''
        
        while n >= 1:
            q, r = divmod(n, 3)
            n = q
            s += str(r)
        
        return s
    
    ternary = base_conversion(n)
    decimal = int(ternary, 3)
    
    return decimal