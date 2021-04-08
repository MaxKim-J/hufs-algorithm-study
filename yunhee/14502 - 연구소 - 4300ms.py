# https://fantastichu.tistory.com/27

import sys,copy
#sys.setrecursionlimit(10000)
#sys.stdin = open('./test.txt', 'r')
input = sys.stdin.readline

lab = []
result = 0
virusList = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 모든 방향으로 바이러스 전파
def virus(x, y, copyed):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if copyed[nx][ny] == 0:
                copyed[nx][ny] = 2
                virus(nx, ny, copyed)
          
# 안전 영역 크기 계산
def safe(curlab):
    cnt = 0
    for i in range(n):
        for j in range(m):
           if curlab[i][j] == 0:
            cnt += 1
    return cnt

def dfs(start, wall):
    global result
    # 울타리가 3개 설치된 경우
    if wall == 3:
        # lab를 curlab에 넣어주고
        curlab = copy.deepcopy(lab)

        # 바이러스를 퍼트린 다음
        for i in range(len(virusList)):
            [virusX, virusY] = virusList[i]
            virus(virusX, virusY,curlab)

        # 안전한 영역을 계산
        result = max(result,safe(curlab))
        return
        
    for i in range(start, n*m):
        x = (int)(i / m)
        y = (int)(i % m)

        if lab[x][y] == 0:
            lab[x][y] = 1
            dfs(i+1, wall+1)
            lab[x][y] = 0

if __name__ == '__main__':
    n,m = map(int,input().split())
    for i in range(n):
        lab.append(list(map(int,input().split())))

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                virusList.append([i,j])

    dfs(0,0)
    print(result)