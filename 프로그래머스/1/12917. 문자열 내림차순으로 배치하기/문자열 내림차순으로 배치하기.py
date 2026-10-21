def solution(s):
    sorted_s = sorted(s, reverse=True)
    lst = ''.join(sorted_s)
    return lst