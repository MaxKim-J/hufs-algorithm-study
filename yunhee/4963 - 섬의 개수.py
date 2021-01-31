# visited = 1 이 아닌 maparr = 0 으로 하는 방법

import sys
from collections import deque

def BFS(i, j):
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        p_route = [(x,y), (x, y-1), (x, y+1), (x-1,y), (x+1,y), (x-1,y-1), (x-1, y+1), (x+1,y-1), (x+1,y+1)]
        for (tx, ty) in p_route:
            if (0<=tx<h and 0<=ty<w) :
                if maparr[tx][ty]:
                    maparr[tx][ty] = 0
                    queue.append((tx,ty))

input = sys.stdin.readline

while (True):
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    maparr = [list(map(int, input().split())) for _ in range(h)]
    nofisland = 0
    
    for i in range(h):
        for j in range(w):
            if maparr[i][j]:
                nofisland +=1
                BFS(i, j)
    
    print(nofisland)