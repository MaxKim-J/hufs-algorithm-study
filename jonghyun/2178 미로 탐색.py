from collections import deque

U,R,D,L=0,1,2,3
dc=-1,0,1,0
dr=0,1,0,-1

#input
n,m=map(int,input().split(" "))
field=[[0 for i in range(m)] for j in range(n)]

for i in field:
    row=input()
    for j in range(m):
        i[j]=int(row[j])


#큐,방문 준비, 초기값 설정
q=deque()
visited=[[0 for i in range(m)] for j in range(n)]
c,r,level=0,0,1

q.append((c,r,level))
visited[c][r]=level

flag_finished=False

#BFS 실행
while len(q):
    target=q.popleft()
    c,r,level=target
    
    for direction in (U,R,D,L):
        new_c,new_r=c+dc[direction],r+dr[direction]
        
        
        #조건 1) 2차원 범위 안에  2) 벽이 아님  3) 방문 X
        if not (0 <= new_c and new_c < n) or not (0 <= new_r and new_r < m):
            continue

        if not field[new_c][new_r]:
            continue

        if visited[new_c][new_r] != 0:
            continue

        q.append((new_c,new_r,level+1));
        visited[new_c][new_r] = level+1;

        #목적지가 큐에 들어갔으면 종료
        if new_c == n-1 and new_r == m-1:
            flag_finished = True
            break

    if flag_finished:
        break

print(visited[n-1][m-1])