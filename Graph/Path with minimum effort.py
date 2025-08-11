from heapq import heappop,heappush
class Solution(object):
    def minimumEffortPath(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        list1=[[float('inf')]*cols for i in range(rows)]
        list1[0][0]=0
        queue=[(0,0,0)]
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            e,r,c=heappop(queue)
            if r==rows-1 and c==cols-1:
                return e
            for dr,dc in d:
                row=dr+r
                col=dc+c
                if row<0 or row>=rows or col<0 or col>=cols:
                    continue
                e1=max(e,abs(matrix[row][col]-matrix[r][c]))
                if e1<list1[row][col]:
                    list1[row][col]=e1
                    heappush(queue,(e1,row,col))
        return 0
