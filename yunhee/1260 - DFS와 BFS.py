# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 정점 번호는 1번부터 N번 # N == node

import sys

def DFS(root):
    visited = []
    stack = [root]

    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(sorted(graph[now], reverse=True)) #pop은 뒤에서부터니까~
        
    for i in visited:
        print(i, end=' ')

def BFS(root):
    visited = []
    queue = [root]

    while queue:
        now = queue.pop(0) # pop(0) 하면 deque의 popleft가 가능했네!
        if now not in visited:
            visited.append(now)
            queue.extend(sorted(graph[now]))
    for i in visited:
        print(i, end=' ')

input = sys.stdin.readline

# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
node, edge, root = map(int, input().split())

graph = {i+1: [] for i in range(node)}

for i in range(edge):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

DFS(root)
print()
BFS(root)

# 사실 DFS, BFS 안에서 print 안하고 이렇게 해도 됨! ofc return visited 하고 ! 
# print(' '.join(map(str,dfs())))
# print(' '.join(map(str,bfs())))