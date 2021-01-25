def make_subseq(sub, subset, level_max, level_now):
    #지금 만들어진 부분수열, 만든 부분수열의 집합, ...
    subset.append(sub[:])
    print(sub)
    for i in range(level_now, level_max):
        sub.append(i)
        make_subseq(sub,subset,level_max,i+1)
        sub.pop(len(sub)-1)
        
n,s=map(int, input().split(" "))
seq=list(map(int,input().split(" ")))

sub=[]
subset=[]

make_subseq(sub, subset, n, 0)

subset=subset[1:]       #맨 앞에는 크기가 0인 부분수열이 있으므로
print(subset)
count=0
for i in subset:
    sum=0
    for j in i:
        sum+=seq[j]
    if sum==s:
        count+=1
        
print(count)