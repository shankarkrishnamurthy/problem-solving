from bisect import bisect_left as bl
from bisect import bisect as br

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1 = bl(nums,target)
        idx2 = br(nums,target)
        print idx1,idx2
        idx1 = idx1 if idx1 < len(nums) and nums[idx1] == target else -1
        idx2 = idx2-1 if idx2 and nums[idx2-1] == target else -1
        return [idx1,idx2]

print Solution().searchRange([5, 7, 7, 8, 8, 10],8)
print Solution().searchRange([5, 7, 7, 8, 8, 10],9)
print Solution().searchRange([5, 7, 7, 8, 8, 10],5)
print Solution().searchRange([],5)
print Solution().searchRange([0],0)
print Solution().searchRange([1],0)
