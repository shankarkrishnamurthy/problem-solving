from bisect import bisect_left as bl
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #print nums, target
        if not nums: return -1
        if len(nums) < 2: 
            return 0 if nums[0] == target else -1
        lo = 0
        hi = len(nums)
        if nums[lo] < nums[hi-1]: 
            idx = bl(nums,target)
            return idx if idx < len(nums) and nums[idx] == target else -1
        change = True
        while lo < hi and change:
            mid = (lo + hi)//2
            if nums[mid] < nums[lo]:
                hi = mid+1
            else:
                lo = mid
            if mid == (lo+hi)//2: change = False
            #print lo, mid, hi
        idx1 = bl(nums,target,mid,len(nums))
        idx2 = bl(nums,target,0,mid)
        if idx1 < len(nums) and nums[idx1] == target: return idx1
        if idx2 < len(nums) and nums[idx2] == target: return idx2
        return -1

print Solution().search([4,5,6,7,0,1,2], 6)
print Solution().search([4,5,6,7,0,1,2,3], 6)
print Solution().search([4,5,6,7,0,1], 6)
print Solution().search([4,5,6,7,0], 6)
print Solution().search([4,5,6,1], 6)
print Solution().search([4,1,2,3], 6)
print Solution().search([4,1], 6)
