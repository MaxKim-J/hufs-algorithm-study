from itertools import combinations_with_replacement
from itertools import permutations
n= int(input(""))
possible = []
data = [i for i in range(n+1)]
for cwr in combinations_with_replacement(data, 11):
    if sum(cwr) == n:
        #p = list(permutations(list(cwr), 11))
        possible.append(cwr)
print(possible)

