import sys

N = int(input(""))
p = []

for i in range(N):
    #index 맞춰주기용
    p.append([0])

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(len(a)):
        p[i].append(a[j])

def paper(start, end, checknum):
    if double_break:
        ve
    one = 0
    minus = 0
    zero = 0
    c_num = N//3
    #for start in range(1, N, c_num):
    #    for start2 in range(1, N, c_num):
    save = p[start][end]
        #자른 종이 한장
        for i in range(start, c_num+1):
            for j in range(end, c_num+1):

                if p[i][j] != save:
                    paper(start, end, c_num)
                    p(start + c_num, end, c_num)
                    p(start + 2 * c_num, end, c_num)
                    p(start, end + c_num, c_num)
                    p(start + c_num, end + c_num, c_num)
                    p(start + 2 * c_num, end + c_num, c_num)
                    p(start, end + 2 * c_num, c_num)
                    p(start + c_num, end + 2 * c_num, c_num)
                    p(start + 2 * c_num, end + 2 * c_num, c_num)
                    double_break = True  # 탈출!
                    break


                else:
                    if p[i][j] == 1:
                        one += 1
                    elif p[i][j] == -1:
                        minus += 1
                    else:
                        zero += 1
    return minus, zero, one

minus, zero, one = paper(N, minus, zero, one)
print(minus)
print(zero)
print(one)

