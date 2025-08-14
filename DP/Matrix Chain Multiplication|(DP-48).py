class Solution(object):
    def matrixMultiplication(self,a):
        def f(i,j):
            if i==j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            min1=float('inf')
            for k in range(i,j):
                cost=a[i-1]*a[k]*a[j]+f(i,k)+f(k+1,j)
                min1=min(min1,cost)
            dp[i][j]=min1
            return dp[i][j]
        n=len(a)
        dp=[[-1]*n for i in range(n)]
        return f(1,n-1)
