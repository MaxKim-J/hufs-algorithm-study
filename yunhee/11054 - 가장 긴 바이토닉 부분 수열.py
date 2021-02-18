"""
왼쪽부터 오른쪽 방향으로 LIS 배열 계산
오른쪽부터 왼쪽 방향으로 LIS 배열 계산
각 포지션에서 두 배열을 더한 값에서 -1
최댓값 반환
"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
LD = [0]*N
RD = [0]*N
maxvalue = 0

for lp in range(N):
    rp = -1-lp
    for lr in range(lp):
        if A[lp] > A[lr] and LD[lp] < LD[lr] :
            LD[lp] = LD[lr]
    LD[lp] += 1
    for rl in range(-1, rp, -1):
        if A[rp] > A[rl] and RD[rp] < RD[rl] :
            RD[rp] = RD[rl]
    RD[rp] += 1

for a, b in zip(LD,RD):
    maxvalue = max(maxvalue, a+b-1)

print(maxvalue)