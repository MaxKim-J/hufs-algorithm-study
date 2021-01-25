N, M = map(int, input("").split(" "))
A = list(map(int, input("").split(" ")))
count = 0
# 완전탐색으로 할경우 최악: n(n-1)/2
for i in range(N):
    total = A[i]
    # 숫자 그자체가 구하고자하는 값
    if A[i] == M:
        count += 1
    for j in range(i+1, N):
        #목표값 미만일때 계속 더함
        if (total < M):
            total += A[j]
            #목표값 도달
            if total == M:
                count += 1
        #목표값 초과일때 for문 탈출
        else:
            break
print(count)