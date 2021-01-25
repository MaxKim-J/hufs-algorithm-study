from itertools import combinations
N, M = map(int, input("").split(" "))
A = list(map(int, input("").split(" ")))
count = 0
for i in range(1, N+1):
    possible = combinations(A, i)
    for j in possible:
        if sum(j) == M:
            count+=1
print(count)
