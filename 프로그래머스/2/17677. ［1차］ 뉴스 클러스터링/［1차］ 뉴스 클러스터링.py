from collections import Counter

def solution(str1, str2):
    
    # 전처리 (소문자 만들기)
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두 글자씩 끊어서 리스트로 만들기
    str1_lst = []
    str2_lst = []
    for i in range(len(str1)-1):
        temp1 = str1[i:i+2]
        if temp1.isalpha():
            str1_lst.append(temp1)
        
    for i in range(len(str2)-1):
        temp2 = str2[i:i+2]
        if temp2.isalpha():
            str2_lst.append(temp2)
    
    cnt1 = Counter(str1_lst)
    cnt2 = Counter(str2_lst)
    
    inter = cnt1 & cnt2
    union = cnt1 | cnt2
    
    if len(union) != 0:
        return int((sum(inter.values()) / sum(union.values())) * 65536)
    else:
        return 65536