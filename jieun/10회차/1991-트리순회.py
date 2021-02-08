import sys
from collections import deque
N = int(input())
s ={}
#visited = deque()

#입력받기
for i in range(N):
    root, left, right = sys.stdin.readline().split()
    #그냥 root는 A 고정이므로 아래 함수 호출에서 A로 받아도 됨
    if i == 0:
        s_root = root

    s[root] = [left, right]

'''
#필요한 리스트만, 최소화해서 사용하기 
def preorder():
    queue = deque(s_root)
    while queue:
        v = queue.popleft()
        visited.append(v)
        #print(s[v])
        for i in reversed(s[v]):
            if i != '.':
                queue.appendleft(i)
    print("".join(visited))
'''
def preorder(node):
    if node == '.':
        return
    #root
    print(node, end = "")
    #left
    preorder(s[node][0])
    #right
    preorder(s[node][1])

def inorder(node):
    if node == '.':
        return
    #left
    inorder(s[node][0])
    #root
    print(node, end = "")
    #right
    inorder(s[node][1])

def postorder(node):
    if node == '.':
        return
    #left
    postorder(s[node][0])
    #right
    postorder(s[node][1])
    #root
    print(node, end = "")

preorder(s_root)
print()
inorder(s_root)
print()
postorder(s_root)