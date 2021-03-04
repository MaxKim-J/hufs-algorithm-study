import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
start, cnt = 0, 0

for i in range(N):
    A.append(int(input()))

for i in range(N) :
    if A[i] < K:
        continue
    elif A[i] == K:
        start = i
        break
    else:
        start = i-1
        break

if i == N-1 and A[i] < K:
    start = i

for i in range(start,-1,-1):
    quotient = K//A[i]
    K -= A[i]*quotient
    cnt += quotient

print(cnt)