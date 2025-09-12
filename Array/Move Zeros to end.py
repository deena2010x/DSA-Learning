class Solution(object):
    def moveZeroes(self,a):
        n=len(a)
        j=0
        for i in range(n):
            if a[i]!=0:
                a[j]=a[i]
                j+=1
        for i in range(j,n):
            a[i]=0
