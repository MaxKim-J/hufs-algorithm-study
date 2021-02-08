#시간초과
import sys
from collections import deque

N = int(input())

root = [0]*(N+1)
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)


queue = deque([1])
while queue:
    r = queue.popleft()
    for i, v in enumerate(tree[r]):
        if v not in root:
            #print(v)
            root[v] = r
            queue.append(v)

for i in root[2:]:
    print(i)