#bfs
#맞았습니다. but 수행시간이 다른 코드들보다 오래 걸림ㅠㅠ(2740ms)
from collections import deque
import sys


dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if (0 <= x < n) and (0 <= y < m) and (s[x][y] == 1) and ([x,y] not in visited):

                queue.append([x, y])
                visited.append([x, y])
                #print(queue)
                #print(visited)



while True:
    s = []
    queue = deque()
    visited = deque()
    m, n = map(int, sys.stdin.readline().split())
    if (m == 0) and (n == 0):
        break
    for k in range(n):
        s.append(list(map(int, sys.stdin.readline().split())))
    count = 0
    for i in range(n):
        for j in range(m):
            if (s[i][j] == 1) and ([i, j] not in visited):
                queue.append([i, j])
                count += 1
                visited.append([i, j])
                bfs()

    print(count)

#print(s)

