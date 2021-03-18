#문제를 제대로 읽자!
#모음 최소 1개 자음 최소 2개

from itertools import combinations

L, C = map(int, input("").split(" "))
alphabet = input("").split(" ")
alphabet.sort()
result = list(combinations(alphabet, L))


for i in result:
    count = 0
    for j in range(L):
        if (i[j] == 'a') or (i[j] == 'e') or (i[j] == 'i') or (i[j] == 'o') or (i[j] == 'u'):
            count += 1

    if (count>=1) and (count<=(L-2)):
        print("".join(i))