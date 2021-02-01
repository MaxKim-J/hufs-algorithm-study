# 입력값 string보다는 list --> 익은 토마토 1로 바꿔주기
import sys
from collections import deque
#동서남북 함수
def four(num):
    lst = []
    if num % M != 0:
        lst.append(num-1)
    if num % M != M - 1:
        lst.append(num+1)
    if num // M != 0:
        lst.append(num - M)
    if num // M != N-1:
        lst.append(num + M)
    return lst

# 익은 토마토 인덱스 return 함수

def ripe(s):
    visited = deque()
    for i, v in enumerate(s): #4번
        if (v == 1) and (i not in visited):
            visited.append(i)

    return visited


#입력 받기
M, N = map(int, input().split())
s = deque()
count_ripe = 0
count_unripe = 0
for i in range(N):
    line = sys.stdin.readline().split()
    for j in line:
        s.append(int(j))
        if int(j) == 1:
            count_ripe += 1
        if int(j) == -1:
            count_unripe += 1

target = (M * N) - count_unripe
count = 0
while True:
    if count_ripe == target:
        print(count)
        break

    else:
        #이부분에서 시간초과가 나지 않을까..
        #현재 익은 토마토
        tomato = ripe(s)
        #print("current",tomato)
        temp = 0

        for i in tomato:
            new = four(i)
            #새로운 익은 토마토
            #print(new)
            for j in new: #4번
                #print(j, s[j])
                if s[j] == 0:
                    s[j] = 1
                    count_ripe += 1
                    temp += 1
        #더이상 새로운 토마토
        if temp == 0:
            print(-1)
            break
        count += 1


