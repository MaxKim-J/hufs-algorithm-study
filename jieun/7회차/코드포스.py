a, b = map(int, input().split())
s = input()

#print(s)
start, end = 1, a
while start < a:
    if s[0] != s[-1]:
        add_s = s
        break
    elif s[start:end] == s[0:end-start]:
        add_s = s[end-start:end]
        break
    else:
        start += 1
#print(end-start)
print(add_s)
start2 = 0
end2 = len(s)
count = 0
total = s + add_s * (b-1)
#print("t",total)

if len(add_s) == a:
    print(total)
else:
    while (count < b) and end2 < len(total):
        #print(count)
        start2 += len(add_s)
        end2 += len(add_s)
        count += 1
        #print(start2, end2)

    print(total[0:end2])
