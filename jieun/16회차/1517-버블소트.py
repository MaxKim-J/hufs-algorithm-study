#시간초과

import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            count += 1


print(count)