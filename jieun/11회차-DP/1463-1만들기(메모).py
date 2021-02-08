k = int(input())
memo = [-1 for c in range(1000001)]
memo[1] = 0
memo[2] = 1
memo[3] = 1
for i in range(4, k + 1):
    memo[i] = memo[i - 1] + 1
    if (i % 3 == 0):
        if (memo[i // 3] < memo[i]):
            memo[i] = memo[i // 3] + 1
    #elif 하면 82%에서 틀렸습니다.
    #6으로 나누어 떨어질 때는 2로 나누는 것과 3으로 나누는 것 어떤 것이 더 빨리 1을 만들 수 있는지 모르기 때문에 두 가지 경우를 다 판단해야 함
    if (i % 2 == 0):
        if (memo[i // 2] < memo[i]):
            memo[i] = memo[i // 2] + 1

print(memo[k])