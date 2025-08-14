class Solution(object):
    def matrixMultiplication(self,a):
        n=len(a)
        dp=[[0]*n for i in range(n)]
        for i in range(n-2,0,-1):
            for j in range(i+1,n):
                min1=float('inf')
                for k in range(i,j):
                    cost=a[i-1]*a[k]*a[j]+dp[i][k]+dp[k+1][j]
                    min1=min(min1,cost)
                dp[i][j]=min1
        return dp[1][n-1]
