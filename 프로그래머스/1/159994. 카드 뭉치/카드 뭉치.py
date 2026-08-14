def solution(cards1, cards2, goal):
    """
    goal에 있는 단어들을 앞에서부터 하나씩 확인하면서:
        cards1의 맨 앞 단어와 같은가? ➔ cards1에서 꺼냄 (포인터 +1)
        cards2의 맨 앞 단어와 같은가? ➔ cards2에서 꺼냄 (포인터 +1)
        둘 다 아니거나 모자라면? ➔ 만들 수 없음 ("No")
    """
    
    p1 = 0
    p2 = 0
    for word in goal:
        if p1 < len(cards1) and cards1[p1] == word:
            p1 += 1
        
        elif p2 < len(cards2) and cards2[p2] == word:
            p2 += 1
            
        else:
            return "No"
        
    return "Yes"