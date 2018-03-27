from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        kss=deque()
        res=[]
        if k==1 or not nums: return nums
        if k==len(nums): return [max(nums)]
        for i,n in enumerate(nums):
            if kss and kss[0]+k <=i: kss.popleft()
            while kss and nums[kss[-1]]<= n: kss.pop()
            kss.append(i)
            if i<k-1: continue
            res.append(nums[kss[0]])
        return res

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print Solution().maxSlidingWindow([1,3,7,-3,5,3,6,1],3)
print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],2)
print Solution().maxSlidingWindow([1,3,7,-3,5,3,6,1],1)
print Solution().maxSlidingWindow([1],1)

