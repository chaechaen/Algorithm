def solution(absolutes, signs):
    
    add = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            add += absolutes[i]
        else:
            add += -absolutes[i]
    
    return add