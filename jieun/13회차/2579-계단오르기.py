score = []
N = int(input())
for i in range(N):
    s = int(input())
    score.append(N)
def dp(N):
    d =[]
    for j in range(N):
        if j == 0:
            d.append([[0]])
        elif j == 1:
            d.append([[1,0]])
        elif j == 2:
            d.append([[2,0],[2,1]])

        else:
            temp = []
            for k in d[j-2]:
                k_temp = k
                k_temp.append(j)
                temp.append(k_temp)
            for y in d[j-3]:
                y_temp = y
                y_temp.append(j)
                y_temp.append(j-1)
                temp.append(y_temp)
                d.remove(d[j-3])
            d.append(temp)

    return d

print(dp(N))