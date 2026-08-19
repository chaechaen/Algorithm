def solution(s, n):
    lst = []
    
    for c in s:
        if c == ' ':
            lst.append(" ")
            
        elif c.isupper():
            # 대문자 A~Z 순환
            lst.append(chr((ord(c) - ord('A') + n) % 26 + ord('A')))
            
        elif c.islower():
            # 소문자 a~z 순환
            lst.append(chr((ord(c) - ord('a') + n) % 26 + ord('a')))

    res = ''.join(lst)

    return res