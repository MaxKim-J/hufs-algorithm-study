#투포인터로 못할것 같은데,,,
import sys
from _collections import defaultdict
num1, target = map(int, input("").split())
A = list(map(int, sys.stdin.readline().split()))
A = sorted(A)
C = defaultdict(int)
count = 0

for i in range(num1):
    for j in range(i, num1):
        k = sum(A[i:j+1])
        C[k] += 1
        if k == target:
            count += C[k]
print(count)
