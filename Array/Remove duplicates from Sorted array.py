class Solution(object):
    def removeDuplicates(self,a):
        n=len(a)
        j=0
        for i in range(1,n):
            if a[i]!=a[j]:
                a[j+1]=a[i]
                j+=1
        return j+1
