class Solution(object):
    def check(self,a):
        n=len(a)
        for i in range(n-1):
            if a[i]>a[i+1]:
                return False
        return True
