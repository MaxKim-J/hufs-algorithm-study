# 시간초과
# bfs visited 구현해서 추가하기
# permutation 없이 구현해보기

from itertools import permutations
n = int(input())
country = [i for i in range(0, n)]
possible = list(permutations(country, n))
w = []

min = 1000000 * n
for i in range(n):
    line = list(map(int, input().split(" ")))
    w.append(line)
for i in range(len(possible)):
    current = possible[i]
    total = 0
    for j in range(0, n):
        if j == (n-1):
            total += w[current[j]][current[0]]
        else:
            total += w[current[j]][current[j+1]]
    #print(total)
    if total < min:
        min = total

print(w)
print(possible)
print(min)
