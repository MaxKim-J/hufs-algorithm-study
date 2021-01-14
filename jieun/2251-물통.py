from collections import deque
a, b, c = map(int, input().split(" "))
awater = 0
bwater = 0

p = deque([[10, 0]])
temp = p.popleft()
cwater = temp[0]
count = temp[1]
if cwater > (b - bwater):
    bwater = b
    cwater -= (b - bwater)
    