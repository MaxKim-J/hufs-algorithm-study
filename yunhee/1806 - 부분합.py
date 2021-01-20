"""
투포인터 알고리즘
- 인덱스를 가리키는 두 개의 변수(포인터)를 선언하여 사용
- 주로 배열 안에 있는 값들을 연속해서 더하거나 연산하는 경우에 사용
- [5,1,3,5,10]이면 5+1+3이런식으로가다가 S넘으면 왼쪽부터 빼면서 1+3 이렇게 쭉 가서 제일 작은 minlen 찾는 코드
"""

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

# 안정적인 방법 : 맨 아래 주석
if sum(nums) < S :
    print(0)

else :
    patialsum = nums[0]
    minlen = sys.maxsize
    end = 1
    for start in range(N):
        while patialsum < S and end < N:
            patialsum += nums[end]
            end += 1
        if patialsum >= S:
            minlen = min(minlen, end - start)
            # if minlen == 2:
            #     break
            # 두 개가 나오면 그게 최소겠거니 해서 집어넣었으나 틀렸습니다 발생,,!
        patialsum -= nums[start]
    print(minlen)

"""
    if minlen == sys.maxsize:
        print(0)
    else:
        print(minlen)
"""
    