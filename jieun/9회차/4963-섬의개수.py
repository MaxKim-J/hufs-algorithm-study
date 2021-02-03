#bfs
from collections import deque
m, n = map(int, input().split())
s = []

#큐 = 땅
queue = deque()
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
for i in range(n):
    s.append(list(map(int, input().split())))
#print(s)

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if (0 <= x < n) and (0 <= y < m) and (s[x][y] == 1):
                s[x][y] = s[a][b] + 1
                queue.append([x, y])


for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])

bfs()
isTrue = False
result = 0
for i in s:
    for j in i:
        #count가 바뀌지 않고 안 익은 거로 남아 있는 거 판별
        #전체 순회해서 가장 큰 count 찾기
        result = max(result, j)
print(result)