class Solution(object):
    def solve(self,matrix):
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c]!='O':
                return
            matrix[r][c]='#'
            for dr,dc in d:
                row=dr+r
                col=dc+c
                dfs(row,col)
        rows=len(matrix)
        cols=len(matrix[0])
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(rows):
            for j in range(cols):
                if i==0 or j==0 or i==rows-1 or j==cols-1:
                    dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='O':
                    matrix[i][j]='X'
                elif matrix[i][j]=='#':
                    matrix[i][j]='O'
