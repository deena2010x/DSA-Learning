class Solution(object):
    def searchMatrix(self,matrix,target):
        m=len(matrix)
        n=len(matrix[0])
        l=0
        h=m*n-1
        while l<=h:
            m1=(l+h)//2
            r=m1//n
            c=m1%n
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                l=m1+1
            else:
                h=m1-1
        return False
