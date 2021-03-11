# M이 가장 작을 경우를 고려하지 않았음.

N, M, K = map(int, input().split())

pos_maxteam = (N+M-K)//3

if pos_maxteam*2 <= N:
    print(pos_maxteam)

else:
    print(N//2)