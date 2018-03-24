class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ptr = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[ptr]: continue
            ptr += 1
            nums[ptr] = nums[i]
        return ptr + 1
            
print Solution().removeDuplicates([1,1])
print Solution().removeDuplicates([1,1,2])
print Solution().removeDuplicates([2,1,1])
print Solution().removeDuplicates([])
