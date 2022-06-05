class Solution:
    def minMaxGame(self, nums):
        while  len(nums) > 1:
            nn= [0]*(len(nums)//2)
            for j in range(len(nums)//2):
                if j % 2 == 0: nn[j] = min(nums[2*j], nums[2*j+1]) 
                else: nn[j] = max(nums[2*j], nums[2*j+1])
            nums = nn
        return nums[0]
