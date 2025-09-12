class Solution(object):
    def twoSum(self,a,target):
        n=len(a)
        m={}
        for i in range(n):
            rem=target-a[i]
            if rem in m:
                return [m[rem],i]
            m[a[i]]=i
