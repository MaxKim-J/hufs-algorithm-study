import sys
input = sys.stdin.readline

def changeDice(drct, arr):
    if drct == 1:
        return [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif drct == 2:
        return [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif drct == 3:
        return [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]
    elif drct == 4:
        return [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]

N, M, x, y, K = map(int,input().split())

maparr = []
for row in range(N):
    maparr.append(list(map(int, input().split())))

directions = list(map(int, input().split()))
dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in range(len(directions)):
    curdir = directions[i]
    newx = x + dx[curdir]
    newy = y + dy[curdir]
    if not (0 <= newx < N  and 0 <= newy < M) :
        continue
    x, y = newx, newy
    dice = changeDice(curdir, dice)

    if maparr[x][y] == 0:
        maparr[x][y] = dice[6]
    else:
        dice[6] = maparr[x][y]
        maparr[x][y] = 0
    
    print(dice[1])
