# https://www.acmicpc.net/source/27278449 

from sys import stdin

input = stdin.readline
# countSafeCell에 사용되는 상,하,우,좌
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# nearwall에 사용되는, 근처 방향들
d2 = [(-1, -1), (1, 1), (-1, 1), (1, -1), (-1, 0), (1, 0), (0, -1), (0, 1)]


def solve():
    N, M = map(int, input().split())
    board = []
    virus = []
    safeArea = []

    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(len(board[i])):
            if board[i][j] == 2:
                virus.append((i, j))
            elif board[i][j] == 0:
                safeArea.append((i, j))

    def nearWall(_x, _y, _board):
        l, r, u, d = False, False, False, False
        for dx, dy in d2:
            x, y = _x + dx, _y + dy
            if x < 0 or (x < _x and 0 <= y < M and _board[x][y] == 1):
                u = True
            elif x >= N or (x > _x and 0 <= y < M and _board[x][y] == 1):
                d = True
            if y < 0 or (y < _y and 0 <= x < N and _board[x][y] == 1):
                l = True
            elif y >= M or (y > _y and 0 <= x < N and _board[x][y] == 1):
                r = True
            if (l and r) or (u and d):
                return True

        return False

    def countSafeCell(a, b, c):
        _board = [[*board[i]] for i in range(len(board))]
        _board[a[0]][a[1]] = 1
        _board[b[0]][b[1]] = 1
        _board[c[0]][c[1]] = 1

        countSafeArea = len(safeArea) - 3

        # a, b, c 각 자리가 모두 양옆 / 위아래가 벽이나 끝으로 막혀 있어야 확산이 됨.. (???)
        if (nearWall(*a, _board) and nearWall(*b, _board) and nearWall(*c, _board)):
            q = [*virus]
            idx = 0
            while idx != len(q):
                _x, _y = q[idx]
                idx += 1
                for dx, dy in d:
                    x, y = _x + dx, _y + dy
                    if 0 <= x < N and 0 <= y < M and _board[x][y] == 0:
                        q.append((x, y))
                        _board[x][y] = 2
                        countSafeArea -= 1
            return countSafeArea

        return 0

    def buildWall():
        _ans = 0
        # 3중 for문을 통해 3개의 벽 세움
        for i in range(len(safeArea)):
            for j in range(i + 1, len(safeArea)):
                for k in range(j + 1, len(safeArea)):
                    _ans = max(_ans, countSafeCell(safeArea[i], safeArea[j], safeArea[k]))
        return _ans

    return buildWall() # def solve()의 return을 buildWall()로 두어 반복

print(solve())