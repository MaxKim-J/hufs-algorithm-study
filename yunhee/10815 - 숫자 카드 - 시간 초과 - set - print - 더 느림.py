import sys

input = sys.stdin.readline
N = int(input())
Nlist = set(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))

for i in range(M):
    if Mlist[i] in Nlist:
        print(1, end=' ')
    else :
        print(0, end=' ')
