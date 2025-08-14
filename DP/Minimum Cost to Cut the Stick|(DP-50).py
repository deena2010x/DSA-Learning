class Solution(object):
    def minCost(self,n,a):
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            min1=float('inf')
            for k in range(i,j+1):
                cost=a[j+1]-a[i-1]+f(i,k-1)+f(k+1,j)
                min1=min(min1,cost)
            dp[i][j]=min1
            return dp[i][j]
        a=[0]+sorted(a)+[n]
        N=len(a)
        dp=[[-1]*N for i in range(N)]
        return f(1,N-2)
