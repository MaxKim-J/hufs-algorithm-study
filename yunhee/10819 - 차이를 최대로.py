howmany = int(input())
elems = list(map(int, input().split()))

"""
순열 알고리즘의 key point : 하나씩 뽑아서 두고, 나머지 리스트에서 다시 재귀해서 그 뽑아 뒀던거랑 하나씩 붙이는 거!

permutation([1,2,3,4],2) = ([1] + permutation([2,3,4],1)) and
([2] + permutation([1,3,4],1)) and ([3] + permutation([1,2,4],1)) and
([4] + permutation([1,2,3],1))
"""

def perm(lst,n):
	ret = []
	if n > len(lst): return ret

	if n==1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)):
			temp = [i for i in lst]
			temp.remove(lst[i]) # 하나씩 뽑아서 두고
			for p in perm(temp,n-1): # 나머지 리스트 재귀
				ret.append([lst[i]]+p) 
	"""
	for example ([20, 1, 15], 3) 이라면 temp에 처음에는 20을 빼고 다시 perm([1,15],2)를 하게 되는데
	이때 결과는 ret = [[1, 15], [15,1]] 여기에 20붙인 [[20,1,15],[20,15,1]] 가 20번째 줄 첫번째 i가 됨!
	soooo 최종적으론 [[20, 1, 15], [20, 15, 1], [1, 20, 15], [1, 15, 20], [15, 20, 1], [15, 1, 20]]
	"""
	return ret

perms = perm(elems, howmany)

max = 0

for p in perms:
    sum = 0
    for j in range(howmany-1):
        sum += abs(p[j] - p[j+1])
    if sum > max :
        max = sum

print(max)