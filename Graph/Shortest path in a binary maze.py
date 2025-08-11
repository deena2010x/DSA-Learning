from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self,matrix):
        n=len(matrix)
        if matrix[0][0]!=0 or matrix[n-1][n-1]!=0:
            return -1
        queue=deque([[1,0,0]])
        vis=[[0]*n for i in range(n)]
        vis[0][0]=1
        d=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        while queue:
            d1,r,c=queue.popleft()
            if r==n-1 and c==n-1:
                return d1
            for dr,dc in d:
                row=dr+r
                col=dc+c
                if row<0 or row>=n or col<0 or col>=n or vis[row][col] or matrix[row][col]!=0:
                    continue
                vis[row][col]=1
                queue.append([d1+1,row,col])
        return -1
