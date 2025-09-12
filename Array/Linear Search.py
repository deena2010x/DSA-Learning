class Solution(object):
    def linearSearch(self,a,target):
        n=len(a)
        for i in range(n):
            if a[i]==target:
                return i
        return -1
