import sys

input = sys.stdin.readline

def merge_sort(start, end):
    global swap, arr
    size = end - start
    if size < 2:
        return
    mid = (start + end) // 2


    # divide
    #리스트의 길이가 1이 될때까지 반으로 잘게 나눈다.
    merge_sort(start, mid)
    merge_sort(mid, end)

    # merge
    new_arr = []
    idx1, idx2 = start, mid
    cnt = 0
    while idx1 < mid and idx2 < end:
        #작은애 append
        if arr[idx1] > arr[idx2]: #첫번째 원소 비교 (오른쪽 리스트 선택 ->swap 일어남)
            new_arr.append(arr[idx2])
            idx2 += 1
            cnt += 1 #swap+=1
        else:  # arr[idx1] < arr[idx2] (왼쪽 리스트 선택 )
            new_arr.append(arr[idx1])
            idx1 += 1
            swap += cnt
    #나머지 처리

    while idx1 < mid: #첫번쨰리스트 뒤로 감 swap 횟수 =count 횟수(이전 횟차에 오른쪽 리스트 누적되어 추가된 숫자)만큼 일어남
        new_arr.append(arr[idx1])
        idx1 += 1
        swap += cnt
    while idx2 < mid:
        new_arr.append(arr[idx2])
        idx2 += 1

    # reflect
    for t in range(len(new_arr)):
        arr[start + t] = new_arr[t]


n = int(input())
arr = list(map(int, input().split()))
swap = 0
merge_sort(0, n)
print(swap)
