class Solution:
    def spiralOrder(self,matrix):
        list1=[]
        t=0
        b=len(matrix)-1
        l=0
        r=len(matrix[0])-1
        while t<=b and l<=r:
            for i in range(l,r+1):
                list1.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                list1.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    list1.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in  range(b,t-1,-1):
                    list1.append(matrix[i][l])
                l+=1
        return list1
