import math

def dp(seq, n):
	if seq[n]!=0:
		pass
	elif(n<=3):
		seq[n]=n
	else:
		closest=int(math.sqrt(n))
		min=100001
		
		for i in range(closest, 0, -1):
			result=dp(seq, n-i*i)+1
			if(result<min):
				min=result
				if(min<=2):
					break
		seq[n]=min
	return seq[n]
		
if __name__=="__main__":
	n=int(input())
	seq=[0 for i in range(n+1)] 
	
	for i in range(100001):
		dp(seq, n)
	
	#print(seq)
	print(seq[n])
