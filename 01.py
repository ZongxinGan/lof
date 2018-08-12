# -*- coding: utf8 -*-
'''
import numpy as np

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve(v,w,weight,n)
    print(result)
'''

def bag(n,c,w,v):  
    res=[[-1 for j in range(c+1)] for i in range(n+1)]  
    for j in range(c+1):  
        res[0][j]=0  
    for i in range(1,n+1):  
        for j in range(1,c+1):  
            res[i][j]=res[i-1][j]  
            if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:  
                res[i][j]=res[i-1][j-w[i-1]]+v[i-1]  
    return res  
  
def show(n,c,w,res):  
    print('最大报酬为:',res[n][c])  
    x=[False for i in range(n)]  
    j=c  
    for i in range(1,n+1):  
        if res[i][j]>res[i-1][j]:  
            x[i-1]=True  
            j-=w[i-1]  
    print('选择的物品编号为:')  
    for i in range(n):  
        if x[i]:  
            print(str(i))  
      
  
if __name__=='__main__':  
    n=5  
    c=10  
    w=[2,2,6,5,4]  
    v=[6,3,5,4,6]  
    res=bag(n,c,w,v)  
    show(n,c,w,res)  