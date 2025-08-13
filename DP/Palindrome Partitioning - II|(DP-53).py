class Solution(object):
    def minCut(self,s):
        def f(i):
            if i==n:
                return -1
            if dp[i]!=-1:
                return dp[i]
            min1=float('inf')
            for j in range(i,n):
                if s[i:j+1]==s[i:j+1][::-1]:
                    cost=1+f(j+1)
                    min1=min(min1,cost)
            dp[i]=min1
            return dp[i]
        n=len(s)
        dp=[-1]*n
        return f(0)
