import sys

# sub, subset은 처음엔 빈 리스트. level_now도 처음엔 0 max만 원래수열길이
# sub를 바꿔가면서 subset에 sub를 그때그때 추가하는 함수
"""
Max가 5일 때 [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 4], [0, 1, 3], [0, 1, 3, 4], [0, 1, 4], [0, 2], [0, 2, 3], [0, 2, 3, 4], [0, 2, 4], [0, 3], [0, 3, 4], [0, 4], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]] *여기서 01234는 인덱스
--> 규칙 : 01234 하나씩 다 넣고, n-1째 자리부터 0124, 그다음엔 013, 그다음엔 014, 그다음엔 02, … 
          그러니까 now가 0일 때 1234, 거기서 또 234, 34, 4 하고 1일 때 234, 2일 때 34같은 느낌
"""

def make_subseq(sub, subset, level_now, level_max, orgseq):
    subset.append(sub[:])
    
    for i in range(level_now, level_max):
        sub.append(orgseq[i])
        make_subseq(sub,subset,i+1, level_max, orgseq)
        sub.pop(len(sub)-1)

input = sys.stdin.readline

N, S = map(int, input().split()) #1 ≤ N ≤ 20, |S| ≤ 1,000,000
Nlist = list(map(int, input().split()))

sub=[]
subset=[]

make_subseq(sub, subset, 0, N, Nlist)
# subset = [[], [-7], [-7, -3], [-7, -3, -2], [-7, -3, -2, 5], [-7, -3, -2, 5, 8], [-7, -3, -2, 8], [-7, -3, 5], [-7, -3, 5, 8], [-7, -3, 8], [-7, -2], [-7, -2, 5], [-7, -2, 5, 8], [-7, -2, 8], [-7, 5], [-7, 5, 8], [-7, 8], [-3], [-3, -2], [-3, -2, 5], [-3, -2, 5, 8], [-3, -2, 8], [-3, 5], [-3, 5, 8], [-3, 8], [-2], [-2, 5], [-2, 5, 8], [-2, 8], [5], [5, 8], [8]]

subset = subset[1:] # 첫 make_subseq에서 sub[:]는 []이므로 (문제에서 "크기가 양수인 부분수열"!!)
count = 0
for i in subset:
    if sum(i) == S:
        count+=1

print(count)
