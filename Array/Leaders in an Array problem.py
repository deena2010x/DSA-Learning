class Solution(object):
    def leaders(self,a):
        n=len(a)
        list1=[]
        max1=float('-inf')
        for i in range(n-1,-1,-1):
            if a[i]>max1:
                list1.append(a[i])
                max1=a[i]
        return list1[::-1]
