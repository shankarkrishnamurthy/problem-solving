class Solution:
    def triangularSum(self, nums):
        while len(nums) > 1:
            for i in range(len(nums)-1):
                nums[i] += nums[i+1]
            nums.pop()
        return nums[0] % 10
