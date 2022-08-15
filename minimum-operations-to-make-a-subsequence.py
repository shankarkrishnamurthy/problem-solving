class Solution:
    def minOperations(self, tgt, arr):
        def LIS(nums):
            a = []
            for i in nums:
                if not a or a[-1]<i:
                    a.append(i)
                else:
                    m = bisect_left(a,i)
                    a[m] = i
            return len(a)
        th, nums = {v:i for i, v in enumerate(tgt)}, []
        for i in arr:
            if i in th: nums.append(th[i])
        return len(tgt) - LIS(nums)
        
