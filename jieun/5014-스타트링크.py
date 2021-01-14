import math
F, S, G, U, D = map(int, input().split(" "))

if (G - S) == 0:
    print(0)
elif (G - S) > 0:
    times = math.ceil((G-S)/U)
    temp = S + times * U
    print(temp)
    if temp == G:
        print(times)
    else:
        if (temp - G) % D != 0 :
            print("use the stairs")
        else:
            num = (temp-G)//D
            print(num, times, num+times)
else:
    times = math.ceil((S-G)/D)
    temp = S - times * D
    if temp == G:
        print(times)
    else:
        if (G - temp) % U != 0 :
            print("use the stairs")
        else:
            num = (G-temp)//U
            print(num, times, num+times)