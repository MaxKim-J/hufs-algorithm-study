import sys, copy
from itertools import combinations
input = sys.stdin.readline

def check(curlab):
    for i in range(N):
        for j in range(M):
            if curlab[i][j] == 2:
                virus(curlab, i, j, 'E')
    cnt0 = 0
    for _ in curlab :
        cnt0 += _.count(0)
    return cnt0

def virus(curlab, i, j, D):
    n, m = i, j
    if D == 'E':
        while(curlab[n][m] !=1):
            if 0 <= m+1 < M :
                m += 1
                if curlab[n][m] != 1:
                    curlab[n][m] = 2
                else: break
            else:
                virus(curlab, i, j, 'W')
                return
        virus(curlab, i, j, 'W')
        return
    elif D == 'W':
        while(curlab[n][m] !=1):
            if 0 <= m-1 < M:
                m -= 1
                if curlab[n][m] != 1:
                    curlab[n][m] = 2
                else: break
            else:
                virus(curlab, i, j, 'S')
                return
        virus(curlab, i, j, 'S')
        return
    elif D == 'S':
        while(curlab[n][m] !=1):
            if 0 <= n+1 < N:
                n += 1
                if curlab[n][m] != 1:
                    curlab[n][m] = 2
                else: break
            else:
                virus(curlab, i, j, 'N')
                return
        virus(curlab, i, j, 'N')
        return
    else:
        while(curlab[n][m] !=1):
            if 0 <= n-1 < N:
                n -= 1
                if curlab[n][m] != 1:
                    curlab[n][m] = 2
                else: break
            else:
                return
        return

N,M = map(int,input().split())
lab = []
for _ in range(N):
    lab.append(list(map(int,input().split())))

zero = []
result = 0
curlab = copy.deepcopy(lab)
for i in range(N):
    for j in range(M):
        if lab[i][j] != 1:
            zero.append((i,j))

for coms in combinations(zero,3):
    for i, j in coms:
        curlab[i][j] = 1
    result = max(check(curlab), result)
    curlab = copy.deepcopy(lab)
print(result)