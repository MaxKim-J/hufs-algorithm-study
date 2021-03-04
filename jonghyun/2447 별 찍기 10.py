import time

def star10(field, n, c, r):
    if n<3:
        return
    
    n=n//3
    for i in range(c+n, c+2*n):
        for j in range(r+n,r+2*n):
            field[i][j]=' '
    
    for i in range(0, 3):
        for j in range(0, 3):
            star10(field, n, c+i*n, r+j*n)

if __name__=="__main__":
    n=int(input())
    
    field=[["*" for j in range(n)]for i in range(n)]
    
    star10(field, n, 0, 0)
    
    for col in field:
        for row_elem in col:
            print(row_elem, end="")
        print()
        time.sleep(0.125)

