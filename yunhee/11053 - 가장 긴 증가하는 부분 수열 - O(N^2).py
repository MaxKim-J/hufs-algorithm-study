# N개의 수들에 대해 자기 자신 전의 모든 수를 다 훑어보는 O(N^2) 알고리즘

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
D = [0]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and D[i]<D[j]:
            D[i] = D[j]
    D[i]+=1

print(max(D))
