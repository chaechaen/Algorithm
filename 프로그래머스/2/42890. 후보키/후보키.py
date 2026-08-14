from itertools import combinations

def solution(relation):
    
    candidates = []
    
    # 조합
    for r in range(1, len(relation[0]) + 1):
        for combi in combinations(range(len(relation[0])), r):
            
            # 최소성 검사
            if any(set(key).issubset(set(combi)) for key in candidates):
                continue # 최소성 X
                
            # 유일성 검사
            unique_check = {tuple(row[i] for i in combi) for row in relation}
            
            # 중복이 제거된 집합의 크기가 원래 행의 개수와 같다면 유일성 만족 -> 중복되면 없어지니까
            if len(unique_check) == len(relation):
                candidates.append(combi) # 후보키로 등록
                
    return len(candidates)