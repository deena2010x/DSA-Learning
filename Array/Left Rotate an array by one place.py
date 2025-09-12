class Solution(object):
    def rotateArrayByOne(self,a):
        n=len(a)
        temp=a[0]
        for i in range(1,n):
            a[i-1]=a[i]
        a[n-1]=temp
