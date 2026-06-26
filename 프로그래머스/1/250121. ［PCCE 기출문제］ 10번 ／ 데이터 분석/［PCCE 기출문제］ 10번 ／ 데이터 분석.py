def solution(data, ext, val_ext, sort_by):
    
    # 열 이름을 인덱스로 바꿔주는 딕셔너리
    col = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    lst = []
    for i in data:
        if i[col[ext]] < val_ext:
            lst.append(i)
    
    # key= 람다함수 덩어리 (정렬 기준)
    lst.sort(key=lambda x: x[col[sort_by]])
    
    return lst