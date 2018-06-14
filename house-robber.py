class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        n = len(nums)
        if not n: return n
        if n < 2: return nums[0]
        dp1,dp2 = [0]*n, [0]*n
        # lets go till n-1 items only
        dp1[0],dp1[1] = nums[0],max(nums[0],nums[1])
        for i in range(2,n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        dp2[1] = nums[1]
        if n>2: dp2[2] = max(nums[1],nums[2])
        for i in range(3,n):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        print "dp1",dp1
        print "dp2",dp2
        return max(dp1[n-2], dp2[n-1])
        

print Solution().rob([3])
print Solution().rob([3,4])
print Solution().rob([4,3])
print Solution().rob([2,3,2])
print Solution().rob([1,2,3,1])
print Solution().rob([1,3,1,3,100])
