import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
A = [] # 1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수

for i in range(N):
    A.append(int(input()))

for i in range(N) :
    if A[i] < K:
        continue
    elif A[i] == K:
        start = i   # start = 0 같은 거 안해줬다고 백준에서는 runtime error(Name Error)발생
        break
    else:
        start = i-1
        break

cnt = 0

for i in range(start,0,-1):
    while K >= A[i]:
        K -= A[i]
        cnt += 1

print(cnt)

