class Solution(object):
    def rotate(self,a,k):
        n=len(nums)
        k%=n
        nums[:]=nums[-k:]+nums[:-k]
