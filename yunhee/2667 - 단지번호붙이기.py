import sys
from collections import deque

def BFS(i,j):
    unit = 0
    queue = deque([(i,j)])
    while queue:
        x, y = queue.pop()
        p_route = [(x,y), (x, y-1), (x, y+1), (x-1,y), (x+1,y)]
        for (tx, ty) in p_route:
            if (0<=tx<N and 0<=ty<N):
                if house[tx][ty] == '1' and visited[tx][ty] == 0:
                    visited[tx][ty] = 1
                    unit +=1
                    queue.append((tx,ty))
    if unit > 0 :
        result.append(unit)

input = sys.stdin.readline

N = int(input()) # 5≤N≤25 인 정사각형
house = [input()[:N] for i in range(N)]
visited = [[False]*N for i in range(N)]
result = []
count = 0

for i in range(N):
    for j in range(N):
        if house[i][j] == '1' and visited[i][j] == 0:
            BFS(i, j)
            count +=1

print(count)
result.sort()
for i in result:
    print(i)