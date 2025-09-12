class Solution(object):
    def secondLargestElement(self,a):
        n=len(a)
        largest=a[0]
        slargest=-1
        for i in range(1,n):
            if a[i]>largest:
                slargest=largest
                largest=a[i]
            elif a[i]<largest and a[i]>slargest:
                slargest=a[i]
        return slargest
