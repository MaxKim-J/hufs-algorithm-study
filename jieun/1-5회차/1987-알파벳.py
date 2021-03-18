#수정 필요
#bfs, dfs, 백트래킹 풀이 모두가능
#bfs+dfs 풀어보기

ud = [1, -1, 0, 0]
lr = [0, 0, 1, -1]
visited = [False] * 26
R, C = map(int, input("").split(" "))
string = []
for i in range(R):
    a = input("")
    string.append(list(a))
#print(string)


hang = 0
yerl = 0
count = 1
stringnum = ord(string[0][0])-65
visited[stringnum] = True
for i in range(4):
    newhang = hang + ud[i]
    newyerl = yerl + lr[i]
    print(newhang, newyerl)
    if visited[ord(string[newhang][newyerl])-65] == False:
        if (newyerl < C) and (newyerl>=0) and (newhang < R) and (newhang>=0):
            print(ord(string[newhang][newyerl])-65 )
            visited[ord(string[newhang][newyerl])-65] = True
            yerl = newyerl
            hang = newhang
            count+=1
print(visited)
print(count)

