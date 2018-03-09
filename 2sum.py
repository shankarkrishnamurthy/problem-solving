class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vset = set(nums)
        vhash = dict()
        for i,v in enumerate(nums):
            if target-v in vset:
                if not vhash:
                    vhash = {v:k for k,v in enumerate(nums)}
                if vhash[target-v] != i:
                    return [i,vhash[target-v]]
        return []

print Solution().twoSum([1,2, 7, 11, 15],9)   
