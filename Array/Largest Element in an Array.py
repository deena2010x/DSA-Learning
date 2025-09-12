class Solution(object):
    def largestElement(self,a):
        n=len(a)
        largest=a[0]
        for i in range(n):
            if a[i]>largest:
                largest=a[i]
        return largest
