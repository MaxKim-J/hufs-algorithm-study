#랜선 세기
def cnt(number):
    global count
    count = 0
    for k in K_list:
        count += k // number
    return count
#이분탐색
def find(min, max):
    left = min
    right = max

    while left <= right:
        mid = (left + right) // 2

        if cnt(mid) >= N:
            left = mid + 1
        else:
            right = mid - 1
    return right

K, N = map(int, input().split())
K_list = []
for k in range(K):
    K_list.append(int(input()))
K_list.sort()

print(find(1, K_list[-1]))
