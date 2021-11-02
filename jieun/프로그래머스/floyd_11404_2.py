city_num = int(input())
bus_num = int(input())
info = []
max = 10000000
#초기배열 초기화 시키기
info = [[max] * city_num  for i in range(city_num)]
#초기 배열 만들기
for i in range(0, bus_num):
    bus_info = list(map(int, input().split()))
    start, end, cost = bus_info[0], bus_info[1], bus_info[2]
    if cost < info[start-1][end-1]:
        info[start-1][end-1] = cost
#print(info)

#거처가는 노드 비용 반영
#거쳐가는 노드 = i
for i in range(0, city_num):
    #시작 노드 = j
    for j in range(0, city_num):
        #도착노드 = k
        for k in range(0, city_num):
            if (j != k) and (info[j][i] + info[i][k] < info[j][k]):
                info[j][k] = info[j][i] + info[i][k]


for i in info:
    for j in i:
        if j == max:
            print(0, end= " ")
        else:
            print(j, end=" ")
    print()