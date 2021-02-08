#시간초과 
import math
n = int(input())
count = 0
one = n
two = 0

while one >= 0:
    four = 0
    temp = math.factorial(one + two)//(math.factorial(one) * math.factorial(two))
    count += temp
    savetwo = two
    while savetwo >= 1:
        savetwo -= 1
        four += 1
        temp2 = math.factorial(one+savetwo+four) //(math.factorial(one) * math.factorial(savetwo) * math.factorial(four))
        count += temp2
    one -= 2
    two += 1

print(count%10007)