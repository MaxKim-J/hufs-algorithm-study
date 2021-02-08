import sys

input = sys.stdin.readline

def Fastwayto1(N):
    # 틀렸습니다 나온 이유는 N이 1일땐 0이기 때문. 처음에 1이라고 생각해서 틀림.
    if N in (1,2,3):
        return print(1)
    else :
        minc[1],minc[2],minc[3] = 1, 1, 1

    for i in range(4,N+1):
        t1,t2,t3 = sys.maxsize,sys.maxsize,sys.maxsize
        if i%3 == 0 :
            if minc[i//3] != 0:
                t1 = minc[i//3]+1
        if i%2 == 0 :
            if minc[i//2] != 0:
                t2 = minc[i//2]+1
        if minc[i-1] != 0:
            t3 = minc[i-1]+1

        minc[i] = min(t1,t2,t3)
   
    print(minc[N])

N = int(input())
minc = [0] * (N+1)
Fastwayto1(N)