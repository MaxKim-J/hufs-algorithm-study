import sys
from collections import deque

def BFS(root):
    queue = deque([root])

    while queue:
        curnode = queue.popleft()
        if visited[curnode] == 0:
            visited[curnode] = 1
            queue += graph[curnode]

input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for i in range(node+1)]
visited = [0] * (node+1)
count = 0

for i in range(edge):
    idx, neighbor = map(int, input().split())
    graph[idx].append(neighbor)
    graph[neighbor].append(idx)

for i in range(1, node+1):
    if visited[i] == 0 :
        BFS(i)
        count +=1 

print(count)