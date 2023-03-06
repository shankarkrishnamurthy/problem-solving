class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        res, r = set(), len(nums)-1
        nums.sort()
        for i in range(len(nums)//2-1, -1, -1):
            if 2*nums[i] <= nums[r] and r not in res:
                res.add(r), res.add(i)
                r = r - 1
        return len(res)
