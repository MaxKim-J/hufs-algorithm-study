# DP로 구현

import sys
def total(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return total(n-1) + total(n-2) + total(n-3)

n = int(input())
a = [int(sys.stdin.readline()) for i in range(n)]
for i in range(n):
    print(total(a[i]))