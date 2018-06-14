class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2: return nums
        nums.sort()
        dp = [-1]*len(nums) # index of previously divisible number with longest subset
        mdp,mv = [1]*len(nums),0 # max subset ending in 'i', mv holds index of max value
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                print i,j, nums[i], nums[j]
                if nums[i] % nums[j] == 0 and 1 + mdp[j] > mdp[i]:
                    mdp[i] = mdp[j] + 1
                    dp[i] = j
                    mv = i if mdp[i] > mdp[mv] else mv
                    print mdp, dp, mv
        res = []
        while mv >= 0: 
            res.append(nums[mv])
            mv = dp[mv]
        return res[::-1]

print Solution().largestDivisibleSubset([4,8,10,240])
"""
print Solution().largestDivisibleSubset([3])
print Solution().largestDivisibleSubset([])
print Solution().largestDivisibleSubset([1,2,3])
print Solution().largestDivisibleSubset([1,2,4,8])
print Solution().largestDivisibleSubset([2,3,8,5,7,4])
print Solution().largestDivisibleSubset([1,2,3,6,9,12,15,36])
"""
