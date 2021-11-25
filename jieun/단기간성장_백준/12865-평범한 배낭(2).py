#https://gsmesie692.tistory.com/113 참고
import sys

def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(W+1):  # 각 칸을 돌면서
            if i==0 or w==0:  # 0번째 행/열은 0으로 세팅
                K[i][w] = 0
            elif wt[i-1] <= w:  # 점화식을 그대로 프로그램으로
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]], K[i-1][w])  # max 함수 사용하여 큰 것 선택
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


weight = []
val = []
N, K = map(int, sys.stdin.readline().strip().split())
for i in range(N):
    w, v = map(int, sys.stdin.readline().strip().split())
    weight.append(w)
    val.append(v)
print(knapsack(K, weight, val, N))

