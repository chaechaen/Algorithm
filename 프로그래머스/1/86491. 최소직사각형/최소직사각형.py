def solution(sizes):
    for s in sizes:
        s.sort(reverse=True)
    
    first_lst = []
    last_lst = []
    for item in sizes:
        first_lst.append(item[0])
        last_lst.append(item[1])
        
    return max(first_lst) * max(last_lst)