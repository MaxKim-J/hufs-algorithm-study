from sys import stdin
num1 = int(stdin.readline())
N = sorted(map(int,stdin.readline().split()))
num2 = int(stdin.readline())
M = map(int,stdin.readline().split())

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


for i in M:
    print(binary(i), end= " ")