#시간초과
n=int(input())
dp=[0 for _ in range(n+1)]
if n= (1 or 2):
    print(1)
else:
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])