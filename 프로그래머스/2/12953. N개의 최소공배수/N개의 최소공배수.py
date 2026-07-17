import math
from functools import reduce

def solution(arr):
    return reduce(math.lcm, arr)