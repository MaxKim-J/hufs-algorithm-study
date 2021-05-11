from sys import stdin

def row_solve(arr):
    global result
    chk = [[0] * N for _ in range(N)] # 경사로가 겹치지 않기 위한 장치
    for i in range(N):
        j = 0
        going = True
        while j < N-1:
            if arr[i][j] == arr[i][j+1]:
                j+=1
                continue
            # 높은 곳에서 낮은 곳으로 가는 경우
            elif arr[i][j] - arr[i][j+1] == 1:
                if arr[i][j+1:j+1+L].count(arr[i][j+1]) == L:
                    chk[i][j+1:j+1+L] = [1] * L
                    j = j + L
                    continue
                else:
                    going = False
                    break
            # 낮은 곳에서 높은 곳으로 가는 경우
            elif arr[i][j] - arr[i][j+1] == -1:
                if arr[i][j+1-L:j+1].count(arr[i][j]) == L and 1 not in chk[i][j+1-L:j+1]:
                    chk[i][j+1-L:j+1] = [1] * L
                    j +=1
                    continue
                else:
                    going = False
                    break
            else:
                going = False
                break
        if going:
            result +=1

input = stdin.readline
N, L = map(int, input().split())
maparr = [list(map(int, input().split())) for _ in range(N)]
result = 0
row_solve(maparr)
row_solve(list(zip(*maparr))) # zip을 이용한 transpose (전치행렬)
print(result)