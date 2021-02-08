import sys
N = int(input())
tree ={}
for i in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]
