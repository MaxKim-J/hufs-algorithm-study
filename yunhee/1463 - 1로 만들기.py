#https://infinitt.tistory.com/247
import sys
input = sys.stdin.readline

N = int(input())
minc = [0] * (N+1)

for i in range(2, N+1):
    minc[i] = minc[i-1] + 1  

    if i%2 == 0 and minc[i] > minc[i//2] + 1 :
        minc[i] = minc[i//2] + 1
        
    if i%3 == 0 and minc[i] > minc[i//3] + 1 :
        minc[i] = minc[i//3] + 1
        
print(minc[N])
