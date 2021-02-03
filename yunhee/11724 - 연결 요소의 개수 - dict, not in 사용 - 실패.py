import sys
from collections import deque

def BFS(root):
    queue = deque([root])

    while queue:
        curnode = queue.popleft()
        if curnode not in visited:
            visited.append(curnode)
            queue += graph[curnode] # append가 아니라 += 이렇게 해도 됨!
            # 첫번째 예시에서 6은 key가 아니라 keyerror --> 양방향 각각 저장하는 걸로 바꾸기

input = sys.stdin.readline

node, edge = map(int, input().split())
graph = {}
visited = []
count = 0

for i in range(edge):
    key, value = map(int, input().split())
    if key in graph:
        graph[key].append(value)
    else:
        graph[key] = [value]
# Hmmm graph[value] = [key] 하려고 했는데 그러면 if value in graph 도 해야하잖아...

for i in graph:
    if i not in visited :
        BFS(i)
        count +=1 
