import sys
target = int(input(""))
num1 = int(input(""))
A = list(map(int, sys.stdin.readline().split()))
num2 = int(input(""))
B= list(map(int, sys.stdin.readline().split()))
C = []
D = []
for i in range(num1):
    total = A[i]
    C.append(total)
    for j in range(i+1, num1):
        total += A[j]
        C.append(total)

for i in range(num2):
    total = B[i]
    D.append(total)
    for j in range(i+1, num2):
        total += B[j]
        D.append(total)
C= sorted(C)
D = sorted(D)

#투포인터, A는 처음부터, B는 끝부터

c1= 0
d1 = len(D) - 1
count = 0
while True:
    if (C[c1] + D[d1] == target):
        #count 1개는 보장
        cnt1 = 1
        cnt2 = 1
        # 동일한 부분합 찾기 1 1 4
        while ((c1 + 1 <= (len(C)-1)) and (C[c1] == C[c1 + 1]) ):
            c1 += 1
            cnt1 += 1
        while ((d1 -1 >= 0) and (D[d1] == D[d1 - 1]) ):
            d1 -= 1
            cnt2 += 1
        count += cnt1 * cnt2
        c1 += 1

    #목표값보다 작으니 다음으로 더 큰 부분합을 더 해주자
    if ((c1 <= (len(C)-1)) and (d1 >= 0) and ((C[c1] + D[d1]) < target)):
        c1 += 1
    # 목표값보다 크니 다음으로 더 작은 부분합을 더 해주자
    if ((c1 <= (len(C)-1)) and (d1 >= 0) and ((C[c1] + D[d1]) > target)):
        d1 -= 1
    if ((c1> (len(C)-1)) or (d1 < 0)):
        break

print(count)