from itertools import permutations
n = int(input())
possible = permutations(list(map(int, input().split(" "))))
result = 0
for n in possible:
    total = 0
    for i in range(len(n)-1):
        total += abs(n[i] - n[i+1])
    result = max(result, total)
print(result)