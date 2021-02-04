import sys
from collections import deque

def BFS(i, j, island):
    queue = deque([(i,j)])
    visited[i][j] = 1
    maparr[i][j] = island

    while queue:
        x,y = queue.popleft()
        for t in range(4):
            tx, ty = x+dx[t], y+dy[t]
            if (0<=tx<N) and (0<=ty<N):
                if (visited[tx][ty] == 0) and maparr[tx][ty]:
                    visited[tx][ty] = 1
                    maparr[tx][ty] = island
                    queue.append((tx,ty))
                elif maparr[tx][ty] == 0 and not (x,y) in seaside:
                    seaside.append((x,y)) 

def Bridge():
    count = 0
    distance = sys.maxsize
    while seaside:
        count +=1
        for _ in range(len(seaside)):
            oi, oj = seaside.popleft()
            for t in range(4):
                tx, ty = oi+dx[t], oj+dy[t]
                if (0<=tx<N) and (0<=ty<N):
                    if maparr[tx][ty] == 0:
                        maparr[tx][ty] = maparr[oi][oj]
                        seaside.append((tx,ty))
                    # 이전 단계에서 각자 한 개씩 둬서 연결된 경우
                    elif maparr[tx][ty] > maparr[oi][oj]:
                        distance = min(distance, (count-1)*2)
                    # 같은 단계에서 한 섬에 의해 다리가 연결된 경우
                    elif maparr[tx][ty] < maparr[oi][oj]:
                        distance = min(distance, count*2-1)

    return distance

input = sys.stdin.readline

N = int(input())
maparr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
island = 1
seaside = deque()

for i in range(N):
    for j in range(N):
        if (visited[i][j] == 0) and (maparr[i][j] == 1):
            BFS(i, j, island)
            island += 1

print(Bridge())
