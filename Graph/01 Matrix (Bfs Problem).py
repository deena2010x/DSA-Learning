from collections import deque
class Solution(object):
    def updateMatrix(matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        list1=[[float('inf')]*cols for i in range(rows)]
        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    list1[i][j]=0
                    queue.append([i,j])
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            r,c=queue.popleft()
            for dr,dc in d:
                row=dr+r
                col=dc+c
                if row<0 or row>=rows or col<0 or col>=cols or list1[row][col]<=list1[r][c]+1:
                    continue
                list1[row][col]=list1[r][c]+1
                queue.append([row,col])
        return list1
