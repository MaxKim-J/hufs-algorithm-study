import math
n = int(input())
count = 0
one = n
two = 0

while one >= 0:
    temp = math.factorial(one + two)//(math.factorial(one) * math.factorial(two))
    count += temp
    one -= 2
    two += 1

print(count%10007)