# 예시 출력은 그대로 나오는데 틀렸습니다...
# 38번째 줄 조건에 maparr[i][j] == 1 추가했더니 정답

import sys
from collections import deque

def BFS(i, j):
    queue = deque([(i,j)])
    result = 0
    while queue:
        x, y = queue.popleft()
        p_route = [(x,y), (x, y-1), (x, y+1), (x-1,y), (x+1,y), (x-1,y-1), (x-1, y+1), (x+1,y-1), (x+1,y+1)]
        for (tx, ty) in p_route:
            if (0<=tx<h and 0<=ty<w) :
                if visited[tx][ty] == 0:
                    visited[tx][ty] = 1
                    if maparr[tx][ty] == 1:
                        result +=1
                        queue.append((tx,ty))
    if result == 0:
        return False
    else : return True

input = sys.stdin.readline
results = []
while (True):
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    maparr = []
    visited = [ [0]*w for _ in range(h) ]
    nofisland = 0
    for i in range(h):
        maparr.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and maparr[i][j] == 1:
                isisland = BFS(i, j)
                if isisland == True:
                    nofisland +=1
    results.append(nofisland)

for i in results:
    print(i)

# 그냥 while에서 print(nofisland)했는데 테스트 시 출력이 안 나오길래 results를 만들어 출력 했으나,, 그렇게 해도 정답처리 됨