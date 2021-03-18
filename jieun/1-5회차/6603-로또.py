#로또 번호 겹치는거 표시안해줘도 됨
#굳이 deque로 안풀어도 될듯?
#출력을 저렇게만 해야하는 걸까?

from itertools import combinations
from collections import deque
possible = deque([])

while True:
    numlist = list(map(int, input("").split(" ")))
    if numlist[0] == 0:
        break
    else:
        count = numlist[0]
        nums = numlist[1:]
        result = list(combinations(nums, 6))
        possible.append([result])



while possible:
    line = possible.popleft()
    for i in line[0]:
        for j in range(6):
            print(i[j], end=" ")
        print("")
    print(" ")
