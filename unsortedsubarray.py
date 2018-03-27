class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums,
        l = 0
        r = len(nums)-1
        while l < r:
            moved = False
            if l < len(nums)-1 and nums[l+1] >= nums[l]:
                moved = True
                l += 1
            if r > 0 and  nums[r-1] <= nums[r]:
                moved = True
                r -= 1
            if not moved: 
                maxval = max(nums[l:r+1])
                minval = min(nums[l:r+1])
                print "l", l,"r",r,"max", maxval, "min", minval, nums[l:r],
                while r < len(nums)-1 and nums[r+1] < maxval: r += 1
                while l > 0 and nums[l-1] > minval: l -= 1
                break
        print (l,r),":",
        return r-l+1 if r > l else 0

print Solution().findUnsortedSubarray([])
print Solution().findUnsortedSubarray([1])
print Solution().findUnsortedSubarray([2,1])
print Solution().findUnsortedSubarray([1,2])
print Solution().findUnsortedSubarray([0,2,1,4])
print Solution().findUnsortedSubarray([6,8,10,12,14])
print Solution().findUnsortedSubarray([4,6,8,10,12,14])
print Solution().findUnsortedSubarray([-2,0,2,1,4])
print Solution().findUnsortedSubarray([-2,0,2,1,0,4])
print Solution().findUnsortedSubarray([1,2,4,3,5])
print Solution().findUnsortedSubarray([1,2,4,5,3])
print Solution().findUnsortedSubarray([1,2,5,3,4])
print Solution().findUnsortedSubarray([1,2,3,2,2])
print Solution().findUnsortedSubarray([1,3,2,2,2])
print Solution().findUnsortedSubarray([1,3,2,3,3])
print Solution().findUnsortedSubarray([1,3,5,2,4])

