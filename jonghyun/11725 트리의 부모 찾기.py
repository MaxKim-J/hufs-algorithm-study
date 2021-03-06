from collections import deque

class Node:
    def __init__(self):
        self.parent=0
        self.link=[]
        
n=int(input())

graph=[Node() for _ in range(n)]

for _ in range(n-1):
    node1,node2=map(int, input().split(" "))
    graph[node1-1].link.append(node2-1)     ## @ 1번 노드의 인덱스는 0이 되도록 조정 - 인덱스 조정은 입력, 출력 부분에서만
    graph[node2-1].link.append(node1-1)
    
    
    
q=deque()

##최초의 노드 인덱스를 큐에 넣기
idx_now=0
q.append(idx_now)

while len(q):
    idx_now=q.popleft()
    
    for i in graph[idx_now].link:
        if i == graph[idx_now].parent:      ##현재 노드와 연결되어있는 노드들 중 부모인 노드를 제외한다
            continue
        
        q.append(i)
        graph[i].parent=idx_now
        
#DEBUG
debug_count=1
for i in graph:
    print("num: %d, parent: %d, link: "%(debug_count, i.parent+1) + str(i.link))
    debug_count+=1
        
flag_first_skipped=False
for i in graph:
    if flag_first_skipped:
        print(str(i.parent+1))      ## @ 조정한 인덱스 복귀
    else:
        flag_first_skipped=True