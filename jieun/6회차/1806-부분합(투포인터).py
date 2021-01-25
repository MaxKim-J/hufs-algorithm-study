#아직 못품

N, M = map(int, input("").split(" "))
A = sorted(list(map(int, input("").split(" "))))
mini = N
total = 0
start, end = 0, 0
while start!= N:
    if total > M:
        total -= A[start]
        start += 1
    elif (end == N):
        break
    else:
        #목표값에 아직 도달못함
        total += A[end]
        end += 1

    if (total >= M):
        if (end-start) < mini:
            print(total)
            mini = end - start
    else:
        mini = 0

print(mini)