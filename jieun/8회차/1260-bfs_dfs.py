#런타임에러// 반례: 그래프에 노드가 없을 수 있음
# 1 0 1
from collections import deque

def bfs(graph, root):
    queue = deque([root])
    visited = []
    while queue:
       #print("q", queue)
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            #print(current)
            if current in graph:
                next = sorted(graph[current])
                for j in next:
                    if j not in visited:
                        queue.append(j)
    return " ".join(str(k) for k in visited)

def dfs(graph, root):
    stack = [root]
    visited = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            #print(current)
            #print('g',graph[current])
            if current in graph:
                next = sorted(graph[current], reverse=True)
                for j in next:
                    if j not in visited:
                        stack.append(j)
    return " ".join(str(k) for k in visited)





#그래프 입력형식 맞춰주기!!
graph = {}
N, M, V = map(int, input().split())
for i in range(M):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)
    # 양방향으로 처리 (반대쪽 정점도 딕셔너리에 넣어줌)
    # 최초 등록
    if b not in graph:
        graph[b] = [a]
    # 이후 등록
    elif a not in graph[b]:
        graph[b].append(a)
#print(graph)
print(dfs(graph,V))
print(bfs(graph,V))
