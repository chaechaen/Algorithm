def solution(strings, n):
    
    for s in strings:
        sorted_str = sorted(strings, key=lambda s: (s[n], s))
    
    return sorted_str