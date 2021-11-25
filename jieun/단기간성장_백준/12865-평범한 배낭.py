#튜플도 combination 사용가능
#메모리 초과-완전탐색(combination 남발)

from itertools import combinations
N, K = map(int, input("").split())
weight = []
value = []
answer = []
for i in range(N):
    W, V = map(int, input("").split())
    weight.append(W)
    value.append(V)

for i in range(1, N):
    c = list(combinations(weight, i))
    v = list(combinations(value, i))
    for j in range(len(c)):
        total_w = sum(c[j])
        if total_w <= K:
            answer.append(sum(v[j]))
#print(answer)
print(max(answer))
