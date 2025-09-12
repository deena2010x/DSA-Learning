class Solution:
    def findMaxConsecutiveOnes(self,a):
        n=len(a)
        max1=0
        count=0
        for i in range(n):
            if a[i]==1:
                count+=1
                max1=max(max1,count)
            else:
                count=0
        return max1
