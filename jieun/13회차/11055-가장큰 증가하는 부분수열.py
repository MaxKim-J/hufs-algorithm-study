n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = a[0]
for i in range(1, n):
    s =[]
    for j in range(i-1, -1, -1):
        if a[i] > a[j]:
            s.append(dp[j])
    if s == []:
        dp[i] = a[i]
    else:
        dp[i] = a[i]+ max(s)

print(max(dp))
