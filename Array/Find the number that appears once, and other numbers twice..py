class Solution(object):
    def singleNumber(self,a):
        n=len(a)
        xor=0
        for i in range(n):
            xor^=a[i]
        return xor
