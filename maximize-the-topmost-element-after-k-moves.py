class Solution:
    def maximumTop(self, nums, k):
        n = len(nums)
        if n == 1 and k%2 == 1: return -1
        if k == 0: return nums[0]
        v, v1 = nums[:k-1], -1
        if n > k: v1 = nums[k]
        if not v and v1==-1: return -1
        if not v: v=[-1]
        return max(max(v), v1)
