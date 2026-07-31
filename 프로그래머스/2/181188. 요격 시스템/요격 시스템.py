def solution(targets):
    
    targets.sort(key=lambda x: x[1])
    ans, end = 0, 0
    
    for s, e in targets:
        if s >= end: # 현재 미사일의 시작점이 이전 요격 범위 이상이면 기존 요격으로 커버 불가
            ans += 1 # 기존 발사로 못 맞추니 새 미사일 하나 더 발사 (끝점 직전 발사)
            end = e # 새로운 요격 위치를 이 미사일의 끝점으로 갱신
            
    return ans