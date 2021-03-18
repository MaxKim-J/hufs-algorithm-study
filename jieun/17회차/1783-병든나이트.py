N, M = map(int, input().split())
if N == 1:
    count = 1
elif N == 2:
    count = min(4, (M - 1) // 2 + 1)
elif M < 7:
    count = min(4, M)
else:
    count = (2 + (M - 5)) + 1
print(count)