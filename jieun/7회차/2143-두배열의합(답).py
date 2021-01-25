import sys
from _collections import defaultdict
#키에 대한 값이 없으면 값을 0으로 초기화

T = int(sys.stdin.readline())

a = int(sys.stdin.readline())
listA = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
listB = list(map(int, sys.stdin.readline().split()))

dictA = defaultdict(int)


ans = 0

for i in range(a):
    for j in range(i, a, 1):
        dictA[sum(listA[i:j+1])] += 1

for i in range(b):
    for j in range(i, b, 1):
        ans += dictA[T - sum(listB[i:j+1])]

print(ans)