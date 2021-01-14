from collections import deque


def bfs(N):
    count = 0
    q = deque([[N, count]])

    while q:
        v = q.popleft()
        position = v[0]
        count = v[1]
        if position == K:
            return count

        if (position * 2 <= 100000) and (not visited[position * 2]):
            q.append([position * 2, count + 1])
            visited[position * 2] = True
        if (position + 1 <= 100000) and (not visited[position + 1]):
            q.append([position + 1, count + 1])
            visited[position + 1] = True
        if (position - 1 >= 0) and (not visited[position - 1]):
            q.append([position - 1, count + 1])
            visited[position - 1] = True
    return count


N, K = map(int, input("").split(" "))
visited = [False for _ in range(100001)]
print(bfs(N))
