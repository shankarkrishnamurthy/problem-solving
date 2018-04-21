class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def swap(ll, a,b): 
            t = ll[a]
            ll[a] = ll[b]
            ll[b] = t
        rl = wl = bl = 0
        for i in nums:
            if i == 0: rl +=1
            elif i == 1 : wl +=1
            else: bl +=1
        tp = rl
        for i in range(0,rl):
            if nums[i] == 0: continue
            while nums[tp] != 0: tp+=1
            swap(nums, tp, i)
        tp = rl + wl
        for i in range(rl,rl+wl):
            if nums[i] == 1: continue
            while nums[tp] != 1: tp+=1
            swap(nums, tp, i)

#a = [0,1,2]
a = [0,1,2,0,1,0,2,1,2,0,1,1]
#a=[0,1,1,1,1,0]
#a=[1,1,1,1]
Solution().sortColors(a)
print a
