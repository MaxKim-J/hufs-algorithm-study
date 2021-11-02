from math import inf


def solution(n, s, a, b, fares):
    answer = inf
    max = inf
    # 배열 초기화
    info = [[max] * n for i in range(n)]
    for i in fares:
        start, end, cost = i[0], i[1], i[2]
        info[start - 1][end - 1] = cost
        info[end - 1][start - 1] = cost

    # 거처가는 점
    for i in range(n):
        # 시작점
        for j in range(n):
            # 끝나는점
            for k in range(n):
                if j == k:
                    info[j][k] = 0
                if (j != k) and (info[j][i] + info[i][k] < info[j][k]):
                    info[j][k] = min(info[j][k], info[j][i] + info[i][k])
    for i in range(n):
        fee = info[s - 1][i] + info[i][a - 1] + info[i][b - 1]
        answer = min(answer, fee)
    return answer