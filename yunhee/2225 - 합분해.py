# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수

import sys
input = sys.stdin.readline

N, K = map(int,input().split())

dp=[[0]*201 for i in range(201)]

for i in range(1, 201):
    dp[1][i]=1 # K=1이면 N 1개
    dp[2][i]=i+1 # K=2이면 N+1개 

for i in range(2, 201):
    dp[i][1]=i # K에 상관없이 N이 1인 경우에 합이 N이 되는 경우의 수는 K개
    for j in range(2, 201):
        dp[i][j]=(dp[i][j-1]+dp[i-1][j]) % 1000000000

print(dp[K][N])