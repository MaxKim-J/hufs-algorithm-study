#에타토스테네스의 체 + 투포인터

def prime_list(n):
    visited = [True] * (n+1)
    #왜 하나 더 길게할까?
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if visited[i] == True:
            for j in range(i+i, n+1, i):
                visited[j] = False
    return [i for i in range(2, n+1) if visited[i] == True]


N = int(input(""))
lst = prime_list(N)
count = 0
start, end =0, 0
total = 0
while (start != len(lst)):
    if (total > N):
        total -= lst[start]
        start += 1
    elif (end == len(lst)):
        break
    else:
        total += lst[end]
        end += 1

    if total == N:
        count += 1

print(count)