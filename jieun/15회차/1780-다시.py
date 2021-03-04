import sys

N = int(input())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

neg = 0
neut = 0
pos = 0


def p(x, y, n):
    global neg, neut, pos
    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            #다르면 자르기 9-3
            if (paper[i][j] != num_check):
                # 9분면으로 잘라 실행
                for k in range(3):
                    for l in range(3):
                        p(x + k * n // 3, y + l * n // 3, n // 3)
                return
    if (num_check == -1):
        neg += 1
    elif (num_check == 0):
        neut += 1
    else:
        pos += 1


p(0, 0, N)
print(f'{neg}\n{neut}\n{pos}')