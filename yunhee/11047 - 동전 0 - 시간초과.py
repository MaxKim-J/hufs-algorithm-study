import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
A = [] # 1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수
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
    while K >= A[i]:        # 최악의 경우에 이걸 1억번 해야 하기 때문,,
        K -= A[i]
        cnt += 1

print(cnt)

# 1 100000000 과 1로 테스트 해봤을 때 입력 제외 time: 116.85598993301392 몫 사용시 time: 0.0005371570587158203