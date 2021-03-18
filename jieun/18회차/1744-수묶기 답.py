import sys

n = int(sys.stdin.readline())
negative, positive = [], []
zero = 0

for i in range(n):
    m = int(sys.stdin.readline())
    if m <= 0:
        negative.append(m)
    elif m == 0:
        zero += 1
    else:  # m > 0
        positive.append(m)

nl, pl = len(negative), len(positive)
negative.sort()
positive.sort(reverse=True)
res = []
# negative
for i in range(0, nl - 1, 2):
    #1. 음수, 음수 = 곱하기, 2. 음수, 0 = 곱하기
    res.append(negative[i] * negative[i + 1])
#음수가 홀수고 0이 없으면 (-3, -2, -1, 2, 4// -3, -2, -1, 2, 4 , 6) --> 무조건 마지막 음수는 안묶임
if nl % 2 == 1 and zero == 0:
    res.append(negative[nl - 1])
# positive
for i in range(0, pl - 1, 2):
    #1보다 클때 (홀수일 경우 제일 작은 양수 빼고)
    if positive[i] > 1 and positive[i + 1] > 1:
        #4. 양수 양수 곱하기
        res.append(positive[i] * positive[i + 1])
    #1이 있을때
    else:
        #6. 1과 양수면 더하기
        res.extend([positive[i], positive[i + 1]])
#양수가 홀수면
if pl % 2 == 1:
    #마지막에 남은 제일 작은 양수 더하기 5. 0, 제일 작은 양수
    res.append(positive[pl - 1])

print(sum(res))
