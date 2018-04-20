class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print nums,
        idx, nz, l = 0, 0, len(nums)
        while nz < l:
            while idx < l and nums[idx] != 0: idx += 1 
            if idx == l: return
            while nz < l and nums[nz] == 0: nz += 1
            if nz == l: return
            nums[idx], nums[nz], idx, nz = nums[nz], 0, idx+1, nz+1

nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print nums
nums = [0, 0]
Solution().moveZeroes(nums)
print nums
nums = [1, 1]
Solution().moveZeroes(nums)
print nums
nums = [0, 1]
Solution().moveZeroes(nums)
print nums
nums = [1, 0]
Solution().moveZeroes(nums)
print nums
