# 출력 초과
# 2931의 경우 -1 출력해야 하지만 9321 출력

N = input()
sumofdigits = 0

for i in N:
    sumofdigits += int(i)

if sumofdigits%3 == 0:
    print(''.join(sorted(N,reverse=True)))
else:
    print(-1)