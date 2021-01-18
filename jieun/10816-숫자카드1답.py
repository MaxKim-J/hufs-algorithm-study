#이분탐색은 정렬이 되어 있어야함
#시간초과 왜 때문에...?
from sys import stdin
num1 = int(stdin.readline())
N = sorted(map(int,stdin.readline().split()))
num2 = int(stdin.readline())


def binary(target):
    left = 0
    right = num1-1
    while (left <= right):
        mid = (left+right) // 2
        if N[mid] == target:
            return 1
        elif N[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

for num in list(map(int, input().split())):
    print(binary(num), end = ' ')