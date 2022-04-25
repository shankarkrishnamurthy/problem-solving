class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1,len(nums)):
            res = res.intersection(set(nums[i]))
        return sorted(res)
