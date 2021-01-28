import sys
from collections import deque

def BFS():
    queue = deque()
    count = 0 
    for i in range(1, node+1):
        if visited[i] == 0 :
            visited[i] = 1
            queue.append(i)
            count += 1
            while queue:
                curnode = queue.popleft()
                for j in graph[curnode]:
                    if visited[j] == 0:
                        visited[j] = 1
                        queue.append(j)
    print(count)

input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for i in range(node+1)]
visited = [0] * (node+1)

for i in range(edge):
    idx, neighbor = map(int, input().split())
    graph[idx].append(neighbor)
    graph[neighbor].append(idx)

BFS()