def nine_tree(x, y, n):
    global matrix, minus, zero, plus
    type = matrix[y][x]  # 첫 타입과 나머지 타입이 같아야함
    double_break = False  # for문 탈출용 double_break

    for i in range(x, x + n):
        if double_break:
            break

        for j in range(y, y + n):
            if matrix[j][i] != type:  # 하나라도 틀릴시에 재귀문 생성
                k = n // 3

                # 9분면으로 잘라 실행
                nine_tree(x, y, k)
                nine_tree(x + k, y, k)
                nine_tree(x + 2 * k, y, k)
                nine_tree(x, y + k, k)
                nine_tree(x + k, y + k, k)
                nine_tree(x + 2 * k, y + k, k)
                nine_tree(x, y + 2 * k, k)
                nine_tree(x + k, y + 2 * k, k)
                nine_tree(x + 2 * k, y + 2 * k, k)

                double_break = True  # 탈출!
                break

    if not double_break:
        if matrix[y][x] == -1:
            minus += 1
        elif matrix[y][x] == 0:
            zero += 1
        else:
            plus += 1


N = int(input())
matrix = []
minus = 0
zero = 0
plus = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))

nine_tree(0, 0, N)
print(minus)
print(zero)
print(plus)
