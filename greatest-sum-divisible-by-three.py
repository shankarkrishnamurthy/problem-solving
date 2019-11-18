from typing import *
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot,m1a,m2a = sum(nums),[],[]
        for i in nums:
            if i % 3 == 1: 
                if len(m1a)<2: 
                    m1a.append(i)
                    m1a.sort()
                else:
                    if i <= m1a[0]: m1a[0],m1a[1] = i,m1a[0]
                    elif i < m1a[1]: m1a[0],m1a[1] = m1a[0],i
            elif i % 3 == 2: 
                if len(m2a)<2: 
                    m2a.append(i)
                    m1a.sort()
                else:
                    if i <= m2a[0]: m2a[0],m2a[1] = i,m2a[0]
                    elif i < m2a[1]: m2a[0],m2a[1] = m2a[0],i
        c = tot % 3
        print(tot,m1a,m2a,c)
        if c == 1: tot -= min(m1a[0],sum(m2a) if len(m2a) ==2 else float("inf"))
        elif c == 2: tot -= min(m2a[0],sum(m1a) if len(m1a) ==2 else float("inf"))
        return tot
    
print(Solution().maxSumDivThree(nums = [4,1,5,3,1]))
print(Solution().maxSumDivThree(nums = [1,2,3,4,4]))
print(Solution().maxSumDivThree(nums = [4]))
print(Solution().maxSumDivThree(nums = [3,6,5,1,8]))
