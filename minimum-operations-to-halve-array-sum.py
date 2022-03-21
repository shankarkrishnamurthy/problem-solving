from heapq import *
class Solution:
    def halveArray(self, nums):
        k, t, n = 0, 0, 0
        for i in range(len(nums)): nums[i], k = -nums[i], k+nums[i]
        heapify(nums)
        while t > -k/2:
            v, n = heappop(nums), n+1
            t += v/2
            heappush(nums, v/2)
            #print(v, nums)
        return n
