from typing import *
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        a,b = 0,0 # a is min of both neigh and b is max
        for i in range(len(nums)):
            c = b if i % 2 == 1  else a
            if i > 0 and i < len(nums)-1:
                mi = min(nums[i-1],nums[i+1])
                if nums[i] >= mi: c += nums[i] - mi + 1
            elif i > 0:
                if nums[i-1]  <= nums[i]: c += nums[i] -nums[i-1] +1
            else:
                if nums[i] >= nums[i+1]: c += nums[i] -nums[i+1] + 1
            if i %2 ==1: b=c
            else: a = c
            print(i,a,b)
        return min(a,b)
                
print(Solution().movesToMakeZigzag(nums = [9,6,1,6,2]))
print(Solution().movesToMakeZigzag([1,2,3]))
print(Solution().movesToMakeZigzag( [2,7,10,9,8,9]))
print(Solution().movesToMakeZigzag( [3,10,7,9,9,3,6,9,4]))
print(Solution().movesToMakeZigzag( [10,4,4,10,10,6,2,3]))
