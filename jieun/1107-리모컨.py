# 풀지 못했음

right = {str(x) for x in range(11)}

target = int(input())
wrong_num = int(input())
if (wrong_num == 0):
    pass
else:
    break_button = set(input().split())
    right -= break_button

result = abs(target - 100)
for i in range(1000001):
    is_enable = True
    for div_num in str(i):
        if (div_num not in right):
            is_enable = False
    if (is_enable):
        result = min(result, abs(target - i) + len(str(i)))

print(result)