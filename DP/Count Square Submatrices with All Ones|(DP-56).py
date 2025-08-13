class Solution(object):
    def countSquares(self,matrix):
        def f(i,j):
            if matrix[i][j]==0:
                return 0
            if i==0 or j==0:
                return 1
            return 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0]*n for i in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                dp[i][j]=f(i,j)
                count+=dp[i][j]
        return count
