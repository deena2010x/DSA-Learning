class Solution(object):
    def trap(self,a):
        n=len(a)
        lmax=0
        rmax=0
        total=0
        l=0
        r=n-1
        while l<r:
            if a[l]<=a[r]:
                if lmax>a[l]:
                    total+=lmax-a[l]
                else:
                    lmax=a[l]
                l+=1
            else:
                if rmax>a[r]:
                    total+=rmax-a[r]
                else:
                    rmax=a[r]
                r-=1
        return total
