class Solution(object):
    def maxSumAfterPartitioning(self,a,k):
        def f(i):
            if i==n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            length=0
            max1=float('-inf')
            max2=float('-inf')
            for j in range(i,min(i+k,n)):
                length+=1
                max1=max(max1,a[j])
                sum1=length*max1+f(j+1)
                max2=max(max2,sum1)
            dp[i]=max2
            return dp[i]
        n=len(a)
        dp=[-1]*n
        return f(0)
