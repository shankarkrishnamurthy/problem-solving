class Solution:
    def __init__(self):
        self.dp={}

    def do_rob(self, nums, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        if len(nums)==0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if not self.dp.has_key(n):
            v1 = self.do_rob(nums[1:], n-1)
            v2 = nums[0] + self.do_rob(nums[2:],n-2)
            self.dp[n] = max(v1,v2)
        return self.dp[n]

    def rob(self, nums):
        return self.do_rob(nums, len(nums)-1)

s = Solution()
print s.rob([1,7,5,3,8,4,0,9])
print s.dp
