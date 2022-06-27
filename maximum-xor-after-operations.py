class Solution:
    def maximumXOR(self, nums):
        res = nums[0]
        for i in range(1,len(nums)):
            res |= nums[i]
        return res
        
