from itertools import combinations
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
maparr = [list(map(int,input().split())) for _ in range(N)]
chickens, houses, distances = [], [], []

for r in range(N):
    for c in range(N):
        if maparr[r][c] == 1:
            houses.append((r,c))
        elif maparr[r][c] == 2:
            chickens.append((r,c))

comb = list(combinations(chickens, M))

for cases in comb:
    cityChicken = 0
    for h in houses:
        homeChicken = float('inf')
        for c in cases:
            homeChicken = min(homeChicken, abs(h[0]-c[0])+abs(h[1]-c[1]))
        cityChicken += homeChicken
    distances.append(cityChicken)

print(min(distances))