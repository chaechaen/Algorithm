from collections import deque

def solution(files):

    parsed = []
    
    for file in files:
        head = ""
        number = ""
        tail = ""
        
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i] # 숫자 나오면 그 이전까지는 다 head
                
                number_part = file[i:i+5] # number는 최대 5개까지
                num_str = ""
                
                for c in number_part:
                    if c.isdigit():
                        num_str += c
                    else: # 숫자 아닌게 나오면 거기서부터는 tail이므로 종료
                        break
                        
                tail = file[i+len(num_str):] # 나머지는 tail
                number = num_str
                break
                
        parsed.append((head, number, tail))
    
    parsed.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(item) for item in parsed]