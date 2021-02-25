# dp[i] = 카드 i개 구매하는 최대 가격 , Plist[k] = k개가 들어있는 카드팩 가격 이라고 했을때
# dp[i] = p[k] + dp[i - k] 

import sys
input = sys.stdin.readline

N = int(input())                             # (1 ≤ N ≤ 1,000)
Plist = [0] + list(map(int,input().split())) # (1 ≤ Pi ≤ 10,000)
dp = [0] * (N+1)

for i in range(1,N+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + Plist[k])
        print(i-k, dp[i-k])

print(dp[i])