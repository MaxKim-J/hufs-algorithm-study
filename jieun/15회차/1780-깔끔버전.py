import sys
cnt = [0]*3
# -1,0,1값을 cnt에 저장시킨다.
n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def same(x, y, n):
    # x, y서부터 모두 같은 수인 종이인지 확인
    for i in range(x, x+n):
        for j in range(y, y+n):
            if matrix[x][y] != matrix[i][j]:
                return False
    return True


def solve(x, y, n):
    # 모두 같은 수인 종이면 (1. 9 no)
    if same(x, y, n):
        cnt[matrix[x][y]+1] += 1
        # -1을 0 ~ 1을 2로
        return
    m = n//3
    #9개 종이 체크
    for i in range(0, 3):
        for j in range(0, 3):
            # 3으로 나눈 것들로 점점 좁혀 나감
            solve(x+i*m, y+j*m, m)


solve(0, 0, n)
for i in cnt:
    print(i)