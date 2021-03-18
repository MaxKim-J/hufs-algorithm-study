import sys

input = sys.stdin.readline
#dx dy는 뭘까: possible way (+1,+0)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, idx):
    #마지막 글자까지 도착 (K)
    if idx == len(word):
        return 1

    #이게 뭘까,,,,
    if c[x][y][idx] != -1:
        print("이게뭘까", c[x][y][idx])
        return c[x][y][idx]

    #(4,2) [-1, 0, -1, -1, -1] 0으로는 초기화 왜 해...?
    c[x][y][idx] = 0
    #동서남북 방향
    for i in range(4):
        temp_x, temp_y = x, y
        #k = 움직일 수 있는 칸수 1칸 (가능한 위치 찾기)
        for _ in range(k):
            nx = temp_x + dx[i]
            ny = temp_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                #해당 위치에 문자열이 일치하는지 체크
                if a[nx][ny] == word[idx]:
                    c[x][y][idx] += dfs(nx, ny, idx+1)
            temp_x, temp_y = nx, ny
    return c[x][y][idx]

#input 문자열로 저장하기
n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().strip()))
word = list(input().strip())

#첫번째 문자 찾아서 위치를 전부 start에 넣어주기
start = []
for i in range(n):
    for j in range(m):
        if a[i][j] == word[0]:
            start.append([i, j])
#start [[3, 1]]

#c....3차원 배열...?, ans= 가능한 경우의 수
ans =  0
c = [[[-1] * len(word) for _ in range(m)] for _ in range(n)]

#현재 word에 첫번째 글자 B는 하나이므로 루프는 한번
for i in range(len(start)):
    x, y = start[i]
    #첫번째 시작 위치에서 가능한 경우의 수 현재 (x,y)= (4,2)
    ans += dfs(x, y, 1)
print(ans)
'''

import sys

sys.setrecursionlimit(10 ** 9)


def solve(i, j, depth):
    if visit[i][j][depth] >= 0:
        return visit[i][j][depth]

    if table[i][j] != target[depth]:
        visit[i][j][depth] = 0
        return 0

    depth += 1
    if depth == len_target:
        visit[i][j][depth - 1] = 1
        return 1

    cnt = 0
    for t in range(-k, k + 1):
        if t == 0: continue

        it, jt = i + t, j + t
        if 0 <= it < n:
            cnt += solve(it, j, depth)
        if 0 <= jt < m:
            cnt += solve(i, jt, depth)
    visit[i][j][depth - 1] = cnt
    return cnt


n, m, k = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
print(table)
target = sys.stdin.readline().rstrip()
len_target = len(target)

#visit -1 로 전부 초기화
visit = [[[-1] * len_target for j in range(m)] for i in range(n)]
print(visit)
ans = 0
for i in range(n):
    for j in range(m):
        if table[i][j] == target[0]:
            ans += solve(i, j, 0)
print(ans)
'''