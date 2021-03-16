# 테스트케이스는 정답.. 그런데 틀렸습니다..

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
K = int(input())
apple = []
direction = []
for i in range(K):
    row, col = map(int,input().split())
    apple.append([row-1,col-1])
L = int(input())
for i in range(L):
    sec, drct = input().split()
    direction.append((int(sec),drct))

playing = True
time = 0
snake = 1
pos = [0,0]
snakepos = deque([[0,0]])
head = 90
diridx = 0
turningtime = direction[diridx][0]

while playing:
    time +=1
    if head == 0 :
        pos[0] -= 1
    elif head == 90 :
        pos[1] += 1
    elif head == 180 :
        pos[0] += 1
    elif head == 270 :
        pos[1] -= 1
    
    if (pos not in snakepos) and 0 <= pos[0] < N and 0 <= pos[1] < N:
        snakepos.appendleft(pos.copy())
        if pos in apple:
            snake += 1
        else:
            snakepos.pop()
    
        if time == turningtime:
            drct = direction[diridx][1]
            if drct == 'L':
                head = (head-90) % 360
            elif drct == 'D':
                head = (head+90) % 360
            diridx += 1
            if diridx < L:
                turningtime = direction[diridx][0]
    else:
        playing = False

print(time)