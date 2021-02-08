import sys
N = int(sys.stdin.readline())
dp = [0, 1, 2]
mod = 10007
for i in range(3, N + 1):
    dp.append((dp[i - 1] + dp[i - 2])%mod)
sys.stdout.write(str(dp[N]))

