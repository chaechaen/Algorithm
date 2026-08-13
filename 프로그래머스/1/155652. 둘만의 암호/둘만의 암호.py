def solution(s, skip, index):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in skip:
        alphabet.remove(i)
        
    res = ""
    
    for key in s:
        idx = alphabet.index(key)
        res += alphabet[(idx + index) % len(alphabet)]
        
    return res