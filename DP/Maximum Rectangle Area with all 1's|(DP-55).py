class Solution(object):
    def maximalRectangle(self,matrix):
        def f(heights):
            stack=[]
            n=len(heights)
            max1=float('-inf')
            for i in range(n+1):
                while stack and (i==n or heights[stack[-1]]>=(heights[i] if i<n else 0)):
                    height=heights[stack.pop()]
                    if not stack:
                        width=i
                    else:
                        width=i-stack[-1]-1
                    area=width*height
                    max1=max(max1,area)
                stack.append(i)
            return max1
        if not matrix or not matrix[0]:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        heights=[0]*n
        max1=float('-inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            area=f(heights)
            max1=max(max1,area)
        return max1
