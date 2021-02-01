from collections import deque
m, n = map(int, input().split())
s = []
#큐 = 익은 토마토
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(map(int, input().split())))

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            #동서남북에 있는 아직 덜익은 토마토 체크해서
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
                #익은토마토로 바꿔주기, count 동시에...= s
                s[x][y] = s[a][b] + 1
                queue.append([x, y])

#익은 토마토 위치 큐에 넣기
for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])
bfs()
#print(s)
isTrue = False
result = -2
for i in s:
    for j in i:
        #count가 바뀌지 않고 안 익은 거로 남아 있는 거 판별
        if j == 0:
            isTrue = True
        #전체 순회해서 가장 큰 count 찾기
        result = max(result, j)
if isTrue == True:
    print(-1)
#가장 큰 값이 -1이면 count = 0
elif result == -1:
    print(0)
#처음에 익은거가 1이므로 첫번째 시도에서 +1해서 계산하면 count = 2가 됨 (result-1해줘야함)
else:
    print(result - 1)