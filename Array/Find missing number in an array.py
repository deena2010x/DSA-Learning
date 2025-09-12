class Solution(object):
    def missingNumber(self,a):
        n=len(a)
        xor1=0
        xor2=0
        for i in range(n):
            xor1^=(i+1)
            xor2^=a[i]
        return xor1^xor2
