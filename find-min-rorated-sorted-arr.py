from bisect import *
class Solution:
    def findMin(self, nums):
        l,r=0,len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[r] > nums[m]:
                r = m
            else:
                l = m + 1
        return nums[l]

print(Solution().findMin([7]))
print(Solution().findMin([7,6]))
print(Solution().findMin([6,7,0,1]))
print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([11,13,15,17]))
