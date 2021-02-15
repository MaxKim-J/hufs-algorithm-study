# 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾는 bisect_left를 이용한 이진탐색 NlogN 알고리즘

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
D = [A[0]]

for i in range(N):
    if A[i] > D[-1]:
        D.append(A[i])
    else:
        idx = bisect_left(D, A[i])
        D[idx] = A[i]

print(len(D))