import sys
input = sys.stdin.readline
arr = []
dp = []
l = int(input())
for _ in range(l):
    arr.append(int(input()))
for x in range(l):
    if x==0:
        dp.append(arr[0])
    elif x==1:
        dp.append(arr[0]+arr[1])
    elif x ==2:
        dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
    else:
        dp.append(max(dp[x-2] + arr[x] , dp[x-3] + arr[x] + arr[x - 1]))
print(dp.pop())
