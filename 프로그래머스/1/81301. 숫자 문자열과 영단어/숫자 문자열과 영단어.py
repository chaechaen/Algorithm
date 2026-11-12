def solution(s):
    
    match = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    res = []
    
    string = ""
    for i in s:
        if i.isalpha():
            string += i
            for idx, num in enumerate(match):
                if string == num:
                    res.append(str(idx))
                    string = ""
                
        else:
            res.append(i)
            
    return int(''.join(res))