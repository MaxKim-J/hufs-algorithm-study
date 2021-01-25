#시간초과

from itertools import combinations
N, M = map(int, input("").split(" "))
A = sorted(list(map(int, input("").split(" "))))
min = N
for i in range(1, N+1):
    possible = combinations(A, i)
    for j in possible:
        if sum(j) >= M:
            if len(j) < min:
                min = len(j)

print(min)
