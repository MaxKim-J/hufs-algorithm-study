import sys
n = int(input())
L =[]
positive = []
negative = []
zero = []
total = 0
for _ in range(n):
    n = int(sys.stdin.readline())
    if n > 0:
        positive.append(n)
    elif n < 0:
        negative.append(n)
    else:
        zero.append(n)

positive = sorted(positive)
negative = sorted(negative)

totallen = len(positive) + len(negative) + len(zero)

#총 홀수개인데 0 있을때
if (totallen % 2 != 0) and (len(zero)==1):
    leftm = negative[-1] * 0 + positive[0]
    rightm = negative[-1] + 0 + positive[0]
    if leftm > rightm:
        total += leftm
        for i in range(0, len(negative) - 1, 2):
            total += negative[i] * negative[i + 1]
        for j in range(len(positive), 0, -2):
            total += positive[i] * positive[i - 1]
    else:
        total += rightm
        for i in range(0, len(negative), 2):
            total += negative[i] * negative[i+1]
        for j in range(len(positive), 1, -2):
            total += positive[i] * positive[i-1]


#총 홀수개인데 0 없을떄
elif (totallen % 2 != 0) and (len(zero)== 0):
    #만약 음수그룹이 홀수이면
    if len(negative)%2 != 0:
        total += negative[-1]
        for i in range(0, len(negative)-1, 2):
            total += negative[i] * negative[i + 1]
        for j in range(len(positive), 0, -2):
            total += positive[i] * positive[i - 1]
    #만약 양수그룹이 홀수면
    else:
        total += positive[0]
        for i in range(0, len(negative), 2):
            total += negative[i] * negative[i + 1]
        for j in range(len(positive), 1, -2):
            total += positive[i] * positive[i - 1]

#총 짝수개인데 0이 있을때
elif (totallen%2 == 0) and (len(zero) ==1):
    #음수 홀수개, 양수 짝수개 -> 0은 음수랑 묶임
    if len(negative) %2 != 0:
        total += negative[-1] * 0
        for i in range(0, len(negative)-1, 2):
            total += negative[i] * negative[i + 1]
        for j in range(len(positive), 0, -2):
            total += positive[i] * positive[i - 1]
    #음수 짝수개, 양수 음수개 -> 0은 짝수랑 묶임
    else:
        total += positive[0] + 0
        for i in range(0, len(negative), 2):
            total += negative[i] * negative[i + 1]
        for j in range(len(positive), 1, -2):
            total += positive[i] * positive[i - 1]

print(total)
