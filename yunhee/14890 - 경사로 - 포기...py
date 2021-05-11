from sys import stdin
input = stdin.readline

# N*N지도 (2 ≤ N ≤ 100)과 경사로 길이 L (1 ≤ L ≤ N)이 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.
N, L = map(int,input().split())
maparr = []
result = 0

for _ in range(N):
    maparr.append(list(map(int,input().split())))

for i in range(N):
    # 행별탐색
    for j in range(N):
        curcol = maparr[i][j]
        if j != N-1:
            j+=1
            nextcol = maparr[i][j]
        if curcol != nextcol and abs(curcol-nextcol) == 1:
            # 더 작은 수를 만났을 경우
            if (curcol-nextcol) == 1:
                for l in range(1,L):
                    try :
                        j +=1
                        nextcols = maparr[i][j]
                        if nextcol==nextcols : continue
                    except:
                        break
            # 더 큰 수를 만났을 경우
            if (curcol-nextcol) == -1:
                j -= 1 # 현재 nextcol 기준이니까 curcol 기준으로 되돌림.
                for l in range(1,L):
                    try :
                        j -=1 # 아 !!!!!!!! python -1 index먹잖아....
                        precol = maparr[i][j]
                        if curcol==precol : continue
                    except:
                        break
        
    # for j in range(N):