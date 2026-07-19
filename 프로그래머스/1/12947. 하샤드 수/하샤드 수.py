def solution(x):
    
    str_x = str(x)
    lst = []
    
    for i in range(len(str_x)):
        lst.append(str_x[i:i+1])
    
    int_lst = [int(i) for i in lst]  
    add = sum(int_lst)
    
    if (x % add == 0):
        return True
    else:
        return False