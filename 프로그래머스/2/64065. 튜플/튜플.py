from collections import Counter

def solution(s):
    
    lst = s.replace('{', '').replace('}', '').split(',')
    
    cnt = Counter(lst)
     
    sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    
    ans = []
    for key, value in sorted_cnt:
        ans.append(int(key))
        
    return ans