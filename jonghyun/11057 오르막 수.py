def dp(save, n, dec):
    if save[n][dec] != 0:
        return save[n][dec]

    if n == 0:
        save[n][dec] = 1;
    else:
        sum = 0;
        for i in range(0,dec+1):
            sum+=dp(save, n-1, i);
            sum%=10007;
        save[n][dec]=sum;
    
    return save[n][dec]; 

if __name__=="__main__":
    n=int(input())
    
    save=[[0 for j in range(10)] for i in range(n+1)]
    
    result_sum=0
    version="bottom_up"
    
    if version=="top_down":
        for i in range(10):
            result_sum+=dp(save, n-1, i)
    
    elif version=="bottom_up":
        for i in range(n):
            for dec in range(10):
                dp(save, i, dec)
        for i in range(10):
            result_sum+=dp(save, n-1, i)
    
    print(result_sum%10007)