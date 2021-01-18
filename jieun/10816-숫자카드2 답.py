from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
    # 종료 조건: 남은 탐색 범위가 비었으면 종료
        return 0
    mid = (start+end)//2
    if l == N[mid]: # 발견!
        i, j = 1, 1
        while mid-i >= start: #이거 놓침
            if N[mid-i] != N[mid]:
                break
            else: i += 1
        while mid+j <= end:
            if N[mid+j] != N[mid]:
                break
            else: j += 1
        return i + j - 1
    elif l < N[mid]:  # 찾는 값이 더 작으면 중간을 기준으로 왼쪽 값을 대상으로 재귀 호출
        return binary(l, N, start, mid-1)
    else: # 찾는 값이 더 크면 중간을 기준으로 오른쪽 값을 대상으로 재귀 호출
        return binary(l, N, mid+1, end)


n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))