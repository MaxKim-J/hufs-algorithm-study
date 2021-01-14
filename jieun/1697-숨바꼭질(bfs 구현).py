from collections import deque

def bfs(v):
    count = 0
    #리스트: [현재위치, 소요시간]
    q = deque([[v, count]])
    while q:
        v = q.popleft()
        e = v[0]
        count = v[1]
        #중복여부 확인
        if not visited[e]:
            visited[e] = True
            #동생에게 도착
            if e == K:
                return count
            count += 1
            if (e * 2) <= 100000:
                q.append([e * 2, count])
            if (e + 1) <= 100000:
                q.append([e + 1, count])
            if (e - 1) >= 0:
                q.append([e - 1, count])

    return count


N, K = map(int, input().split())
visited = [False] * 100001
print(bfs(N))