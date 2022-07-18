class Solution:
    def maximumSum(self, nums):
        def getsum(n):
            sum = 0
            for digit in str(n): sum += int(digit)      
            return sum
        nums.sort(reverse=True)
        nh, res = defaultdict(int), -1
        for i in range(len(nums)):
            v = getsum(nums[i])
            if v in nh: res = max(res, nums[nh[v]] + nums[i])
            nh[v] = i
        return res
