def solution(n, words):

    # words에서 같은 단어 나오면 걔가 몇 번째로 나온 단어인지 세서
    # ex) tank는 9번째로 나온 단어.
    # 근데 사람이 3명 -> 9%3 해서 나온 나머지를 더해줘?
    # 그리고 끝말이랑 이어지는지도 체크? 
    
    for i in range(1, len(words)):
        # 탈락 조건: 끝말이 안 이어지거나, 이미 앞에서 등장했던 단어인 경우
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [(i % n) + 1, (i // n) + 1] # 탈락자 발생
    
    # 탈락자 없으면
    return [0, 0]