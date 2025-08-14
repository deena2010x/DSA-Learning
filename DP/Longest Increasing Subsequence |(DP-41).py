class Solution:
    def lengthOfLIS(self,a):
        def f(i,prev):
            if i==n:
                return 0
            if dp[i][prev]!=-1:
                return dp[i][prev]
            nottake=f(i+1,prev)
            take=0
            if prev==-1 or a[i]>a[prev]:
                take=1+f(i+1,i)
            max1=max(nottake,take)
            dp[i][prev]=max1
            return dp[i][prev]
        n=len(a)
        dp=[[-1]*(n+1) for i in range(n)]
        return f(0,-1)
