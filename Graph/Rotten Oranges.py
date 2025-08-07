from collections import deque
class Solution(object):
    def orangesRotting(self,graph):
        queue=deque()
        t=0
        f=0
        rows=len(graph)
        cols=len(graph[0])
        for r in range(rows):
            for c in range(cols):
                if graph[r][c]==1:
                    f+=1
                elif graph[r][c]==2:
                    queue.append([r,c])
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        while queue and f>0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in d:
                    row=dr+r
                    col=dc+c
                    if row<0 or row>=rows or col<0 or col>=cols or graph[row][col]!=1:
                        continue
                    graph[row][col]=2
                    queue.append([row,col])
                    f-=1
            t+=1
        if f==0:
            return t
        return -1
