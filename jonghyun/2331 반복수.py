# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:15:57 2021

@author: Jonghyun Park
"""
table=(
		(0, 1, 2, 3, 4, 5, 6, 7, 8, 9 )
		,(0, 1, 4, 9, 16, 25, 36, 49, 64, 81 )
		,(0, 1, 8, 27, 64, 125, 216, 343, 512, 729 )
		,(0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561 )
		,(0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049 )
	)

def myPow(co,ex):
    return table[ex-1][co]
    
def myFunc(num,p):
    sum=0
    while num:
        i=num%10
        sum+=myPow(i,p)
        num=num//10
        
    return sum

a,p=map(int,input().split(" "))
seq=[0]     #인덱스 0은 사용하지 않음
visited=dict()

#수열의 1번: 입력받은 A가 들어간다
seq.append(a)
visited[a]=len(seq)-1

result=value=0
while(True):
    target=myFunc(seq[-1],p)
    
    if(target in visited):
        result_value=visited[target]-1
        break
    
    seq.append(target)
    visited[target]=len(seq)-1
    
print(result_value)

print(seq)
    
        