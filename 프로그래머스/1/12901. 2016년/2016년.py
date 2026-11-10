def solution(a, b):
    cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    add = sum(cal[:a-1]) + b - 1
    
    res = day[add % 7]
    
    return res