import math
from collections import deque
n, m, k = map(int, input().split())
letter = ""
way = deque([])
for i in range(n):
    line = input("")
    letter += line
target = input("")

#인접 위치 반환 함수
def possible(start):
    p = []
    nline = math.ceil(start/n)
    nth = start % m
    if nth == 0:
        nth = m

    #세로줄인접
    for i in range(nline-k, nline+k+1):
        if (i == nline):
            pass
        elif ((i>=1) & (i<=n)):
            p.append((i, nth))

    #가로줄인접
    for j in range(nth-k, nth+k+1):
        if (j == nth):
            pass
        elif ((j >= 1) & (j <= m)):
            p.append((nline, j))
    return p

def arraytotext(a,b):
    index = (a-1) * m + b
    return index

depth = 1
for i in range(len(letter)):
    if target[0]==letter[i]:
        way.append([i+1, depth])
print(way)
for j in range(1, len(target)):
    if len(way)!= 0:
        num = way.popleft()[0]
        for i in range(len(way)+1):
            pway = possible(num)
            print("current %d", num)
            print(pway)
            for g in pway:
                a = g[0]
                b = g[1]
                index = arraytotext(a, b)
                print(index)
                if letter[index-1] == target[j]:
                    depth += 1
                    way.append([index, depth])
                    print([index, depth])
print(len(way))






