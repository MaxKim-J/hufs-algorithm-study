import sys

input = sys.stdin.readline
N = int(input())
Nlist = set(map(int, input().split()))
# set 은 in O(1) list는 O(N) https://lsh424.tistory.com/59 https://dev.plusblog.co.kr/42
M = int(input())
Mlist = list(map(int, input().split()))
result = [0]*M

for i in range(M):
    if Mlist[i] in Nlist:
        result[i] = 1

print(' '.join(map(str,result)))