#3048 --> 2152 --> 448 ms

import sys 
from itertools import combinations 

n, s = map(int, sys.stdin.readline().split()) 
arr = list(map(int, sys.stdin.readline().split())) 
cnt = 0 

for r in range(1, n+1):
    cm = combinations(arr, r)
    # [(-7,), (-3,), (-2,), (5,), (8,)]
    # [(-7, -3), (-7, -2), (-7, 5), (-7, 8), (-3, -2), (-3, 5), (-3, 8), (-2, 5), (-2, 8), (5, 8)]
    # [(-7, -3, -2), (-7, -3, 5), (-7, -3, 8), (-7, -2, 5), (-7, -2, 8), (-7, 5, 8), (-3, -2, 5), (-3, -2, 8), (-3, 5, 8), (-2, 5, 8)]
    # [(-7, -3, -2, 5), (-7, -3, -2, 8), (-7, -3, 5, 8), (-7, -2, 5, 8), (-3, -2, 5, 8)]
    # [(-7, -3, -2, 5, 8)]
    for c in cm:
        if sum(c) == s:
            cnt += 1
            
print(cnt)
