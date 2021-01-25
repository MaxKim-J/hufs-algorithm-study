N, M = map(int, input("").split(" "))
A = list(map(int, input("").split(" ")))
count = 0
total = 0
start, end = 0, 0
while start!= N: #종료조건: start가 마지막 인덱스면 start end 둘다 이동불가
    if total > M: #합이 너무 커짐
        total -= A[start] #그럼 뒤에꺼 빼주자
        start += 1 #빼줬으니 start 한칸 앞으로 이동
    elif (end == N): #end가 마지막인덱스면 끝이니까 break
        break
    else:
        total += A[end] #아직 너무 작음
        end += 1 #뒤에 더해주자
        #목표값 도착
    if (total == M):
        count += 1
print(count)