class Solution(object):
    def longestIncreasingSubsequence(self,a):
        def f(i,prev):
            if i==n:
                return 0
            if dp[i][prev+1]!=-1:
                return dp[i][prev+1]
            nottake=f(i+1,prev)
            take=0
            if prev==-1 or a[i]>a[prev]:
                take=1+f(i+1,i)
            dp[i][prev+1]=max(nottake,take)
            return dp[i][prev+1]
        def build(i,prev,a1):
            if i==n:
                return
            nottake=dp[i+1][prev+1]
            take=0
            if prev==-1 or a[i]>a[prev]:
                take=1+dp[i+1][i+1]
            if take>=nottake:
                a1.append(a[i])
                build(i+1,i,a1)
            else:
                build(i+1,prev,a1)
        n=len(a)
        dp=[[-1]*(n+1) for _ in range(n)]
        f(0,-1)
        a1=[]
        build(0,-1,a1)
        return a1
