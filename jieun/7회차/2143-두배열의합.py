#시간초과
#음수의 경우 처리 못함

import sys
target = int(input(""))
num1 = int(input(""))
A = list(map(int, sys.stdin.readline().split()))
num2 = int(input(""))
B= list(map(int, sys.stdin.readline().split()))
C = {}
total = 0
def twopointer(N, M, lst): #마지막 인덱스, 목표값
    count = 0
    total = 0
    start, end = 0, 0
    while start != N:  # 종료조건: start가 마지막 인덱스면 start end 둘다 이동불가
        if total > M:  # 합이 너무 커짐
            total -= lst[start]  # 그럼 뒤에꺼 빼주자
            start += 1  # 빼줬으니 start 한칸 앞으로 이동
        elif (end == N):  # end가 마지막인덱스면 끝이니까 break
            break
        else:
            total += lst[end]  # 아직 너무 작음
            end += 1  # 뒤에 더해주자
        # 목표값 도착
        if (total == M):
            count += 1
    return count
astart = min(A)
for i in range(astart, target):
    cnt = twopointer(num1, i, A)
    if cnt > 0:
        C[i] = cnt

#print(C)
for k in C.keys():
    target2 = target - k
    cnt2 = twopointer(num2, target2, B)
    #print("목표", target2)
    #print("갯수", cnt2)
    if cnt2 != 0:
        total += (C[k] * cnt2)



print(total)

