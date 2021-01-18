import sys

N = int(sys.stdin.readline())
Nlist = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))
result = [0]*M

for i in range(M):
    if Mlist[i] in Nlist:
        result[i] = 1

print(' '.join(map(str,result)))