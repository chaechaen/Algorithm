def solution(genres, plays):
    
    ans = []
    genre_total = {} # 장르별 총 재생 횟수
    genre_songs = {} # 장르별 재생횟수, 고유번호 모음
    
    for i in range(len(genres)):
        key = genres[i]
        
        if key in genre_total:
            genre_total[key] += plays[i]  # 키가 이미 존재하면 값 더함
        else:
            genre_total[key] = plays[i]   # 키가 처음 등장하면 새로 값 할당
    #	{'classic': 1450, 'pop': 3100}    
    
        if key not in genre_songs:
            genre_songs[key] = []
        genre_songs[key].append((plays[i], i)) # 재생 횟수, 고유 번호
    
    sorted_genre = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True) # 재생 횟수 많은 장르 순 정렬
    
    for g in sorted_genre:
        genre_songs[g].sort(key=lambda x: (-x[0], x[1])) # 재생 횟수 내림차순, 고유 번호 오름차순
        
        for p, i in genre_songs[g][:2]:
            ans.append(i)
            
    return ans