n= int(input(""))
def dfs(current, info, i, j):
    if i == 0:
        current[i] = j
        r = 0
        p = 0
        for i in range(11):
            if current[i] > info[i]:
                r += 10 - i
            else:
                p += 10 - i
            #재귀(left, array)
            #left n