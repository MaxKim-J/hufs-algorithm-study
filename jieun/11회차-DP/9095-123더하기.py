T = int(input())
def dpro(N):
    dp = [0 for i in range(12)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if N>=4:
        for i in range(4,N+1):
            dp[i] = dp[i-3] + dp[i-2] +dp[i-1]
    return dp[N]
for i in range(T):
    N = int(input())
    print(dpro(N))


