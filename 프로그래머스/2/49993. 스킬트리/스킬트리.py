def solution(skill, skill_trees):
    
    cnt = 0
    
    for skill_tree in skill_trees:
        # skill에 포함된 문자 걸러내고 나머지 문자만 남기기
        filtered_tree = "".join([s for s in skill_tree if s in skill])
        
        # 올바른 순서인지 확인하기 위해 skill의 접두사인지 확인
        if skill.startswith(filtered_tree):
            cnt += 1
        
    return cnt