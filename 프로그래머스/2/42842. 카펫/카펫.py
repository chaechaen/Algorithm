def solution(brown, yellow):
    '''
    - width*height - yellow = brown
    - yellow가 최소 1 이상이면, height이 1+2=3 이상이어야 함
    - 그리고 (yellow + brown) % height이 나머지가 0이어야 함 (height이 약수여야 함)
    - width - 2 = yellow가로 , height - 2 = yellow세로 ==> yellow = (width - 2) * (height - 2)
    '''
    
    for height in range(3, yellow + brown + 1): # 최소 3부터
        if (yellow + brown) % height == 0: # height으로 나누어 떨어질 때
            width = (yellow + brown) // height # width를 구함
            if yellow == (width - 2) * (height - 2):
                return [width, height]