e, s, m = map(int, input("").split())
i = 0
if (e == 15):
    e = 0
if (m == 19):
    m = 0
for i in range(1, 7981):
    result = 28 * i + s
    if ((result % 19 == m) &  (result % 15 == e)):
        break
    i += 1
print(result)
