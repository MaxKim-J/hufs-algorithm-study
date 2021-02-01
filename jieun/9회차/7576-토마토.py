# 입력값 string보다는 list --> 익은 토마토 1로 바꿔주기
import sys

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
visited =[]
def ripe(s):
    for i, v in enumerate(s):
        if (v == 1) and (i not in visited):
            visited.append(i)
    return visited



#입력 받기
M, N = map(int, input().split())
s = []
for i in range(N):
    line = sys.stdin.readline().split()
    for j in line:
        s.append(int(j))



no = s.count(-1)
target = (M * N) - no
count = 0
while True:
    #if count > M*N:
     #   print(-1)
     #   break
    if s.count(1) == target:
        print(count)
        break

    else:
        #현재 익은 토마토
        tomato = ripe(s)
        #print("current",tomato)
        for i in tomato:
            new = four(i)
            #새로운 익은 토마토
            #print(new)
            for j in new:
                #print(j, s[j])
                if s[j] == 0:
                    s[j] = 1
        count += 1


