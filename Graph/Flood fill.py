class Solution(object):
    def floodFill(self,graph,sr,sc,color):
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if graph[r][c]!=org_color:
                return
            graph[r][c]=color
            for dr,dc in d:
                row=dr+r
                col=dc+c
                dfs(row,col)
        org_color=graph[sr][sc]
        if org_color==color:
            return graph
        rows=len(graph)
        cols=len(graph[0])
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        dfs(sr,sc)
        return graph
