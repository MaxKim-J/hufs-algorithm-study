def dp(save, n):
	if save[n]!=0:
		pass
	
	if n==1:
		save[n]=1
	elif n==2:
		save[n]=3
	else:
		save[n]=(dp(save, n-1) + dp(save,n-2)*2)%10007
	
	return save[n]

if __name__=="__main__":
    n=int(input())
    save=[0 for _ in range(n+1)]
    
    print(dp(save, n))
    
    