def solution(people, limit):
    
    people.sort()
    
    cnt = 0
    
    left = 0 # 가장 가벼운 사람 인덱스
    right = len(people) - 1 # 가장 무거운 사람 인덱스
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        cnt += 1
        
    return cnt