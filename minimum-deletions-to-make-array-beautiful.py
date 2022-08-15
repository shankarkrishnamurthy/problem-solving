class Solution:
    def minDeletion(self, nums):
        n, dp, c = len(nums), nums[0], 1
        for i in range(1, n):
            if c % 2 == 0 or dp != nums[i]:
                dp, c = nums[i], c+1
            #print('i', i, 'dp' ,dp)
        return len(nums) - c + c % 2
