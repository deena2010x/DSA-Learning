class Solution(object):
    def check(self,a):
        n=len(a)
        drop=False
        for i in range(n):
            if a[i]>a[(i+1)%n]:
                if drop:
                    return False
                drop=True
        return True
