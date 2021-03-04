p,*o=open(0)
k=int(p[2:])
c=0
for i in map(int,o[::-1]):c+=k//i;k=k%i
print(c)