# 틀렸습니다
# 10000까지는 괜찮은데 너무 시간오래걸림
# 반례 찾지 못함
# visited 구현해서 수정 필요함

subin, sister = map(int, input().split(" "))
possible = [[subin]]
visited = [False] * 100001
if subin == sister:
    print(0)
else:
    for i in range(100001):
        next = []
        for j in range(len(possible[i])):
            a = 2 * (possible[i][j])
            b = (possible[i][j]) - 1
            c = (possible[i][j]) + 1
            if (a <= 100000) :
                next.append(a)
            if (b >= 0):
                next.append(b)
            if (c <= 100000) :
                next.append(c)
        if sister in next:
            print(i+1)
            break
        else:
            possible.append(next)
    print(possible)
