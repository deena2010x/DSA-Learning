class Solution(object):
    def maxCoins(self,a):
        def f(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            max1=float('-inf')
            for k in range(i,j+1):
                cost=a[i-1]*a[k]*a[j+1]+f(i,k-1)+f(k+1,j)
                max1=max(max1,cost)
            dp[i][j]=max1
            return dp[i][j]
        a=[1]+a+[1]
        n=len(a)
        dp=[[-1]*n for i in range(n)]
        return f(1,n-2)
