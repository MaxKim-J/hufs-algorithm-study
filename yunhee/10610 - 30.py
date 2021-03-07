N = input()
N = ''.join(sorted(N,reverse=True))
sumofdigits = 0

if N[-1] != '0':
    print(-1)

else:
    # sum(map(int,N[:-1]))도 가능. then sumofdigits 필요 없져..~
    for i in N[:-1]:
        sumofdigits += int(i)

    if sumofdigits%3 == 0:
        print(N)
    else:
        print(-1)