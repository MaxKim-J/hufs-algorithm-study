"https://peisea0830.tistory.com/40"

import sys

input = sys.stdin.readline

N, S = map(int, input().split()) #1 ≤ N ≤ 40, |S| ≤ 1,000,000 and 시간제한 1초
Nlist = list(map(int, sys.stdin.readline().split()))

M = N//2
N = N - M

Left = [0] * (1<<N) # (1<<3) == 8 == 2**3 : 가능한 집합의 개수, 0b1 --> 0b1000

# 비트마스킹을 이용하여 Subset의 합을 담는다
# Nlist = [-7, -3, -2, 5, 8], N = 3일 때 Left = [0, -7, -3, -10, -2, -9, -5, -12]
for i in range(1<<N):
    for k in range(N):
        if (i&(1<<k)) > 0:     
            Left[i] += Nlist[k]

Right = [0]*(1<<M)
for i in range(1<<M):
    for k in range(M):
        if (i&(1<<k)) > 0:
            Right[i] += Nlist[k+N]
            
# Left 오름차순 정렬, Right 내림차순 정렬
Left.sort()
Right.sort(reverse = True)

N,M = (1<<N), (1<<M) # Left의 길이, Right의 길이
i, j, ans = 0, 0, 0 # Left, Right의 pointer와 answer

while i < N and j < M:
    # Left = [-12, -10, -9, -7, -5, -3, -2, 0]
    # Right = [13, 8, 5, 0]
    # 같은 경우
    if Left[i] + Right[j] == S:
        # i,j를 이동
        c1 = 1
        c2 = 1
        i += 1
        j += 1
        # 예외 처리
        """예를 들어 Left = [-10, -10, -8], Right = [13, 8, 5] 인데 S = 3일 경우에 
            i=0, j=0인 상태에서 Left[i] + Right[j] == S 이므로
            이때 i=1, j=1로 동시에 이동하는 건데! 이렇게 가면 i=1, j = 1인 경우를 넘어가니까
            c1 +=1 해주고 c1*c2로 반영 후 i+=1로 i=3으로 넘어가는 ! """
        while i < N and Left[i] == Left[i-1]:
            c1 += 1
            i += 1
        while j < M and Right[j] == Right[j-1]:
            c2 += 1
            j += 1

        ans += c1*c2 # 전체 순서쌍 반영
        
    # 작은 경우 i만 이동
    elif Left[i] + Right[j] < S:
        i += 1
        
    # 큰 경우 j만 이동
    else:
        j += 1
        
# S가 0인 경우 공집합의 경우를 빼줘야 하므로 1감소
if S == 0:
    ans -= 1
    
print(ans)