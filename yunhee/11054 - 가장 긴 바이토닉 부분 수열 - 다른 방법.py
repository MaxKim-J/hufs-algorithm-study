import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
plus=[1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            if plus[i]<=plus[j]+1:
                plus[i]=plus[j]+1
minus=plus # 불필요. 얕은 복사. 깊은복사 : minus = list(plus)
for i in range(1,n):
    for j in range(i):
        if arr[i]<arr[j]:
            if minus[i]<=minus[j]+1:
                minus[i]=minus[j]+1
print(max(minus))

# arr: [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
# plus: [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
# minus: [1, 2, 3, 4, 3, 4, 4, 5, 6, 7]