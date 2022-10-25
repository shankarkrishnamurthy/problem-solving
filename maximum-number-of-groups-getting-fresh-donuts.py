class Solution:
    def maxHappyGroups(self, gbs, nums):
        @lru_cache(None)
        def ksum(i, k, tgt):
            if k == 0 and tgt == 0: return True
            if tgt < 0 or k <= 0 or i >= len(nums): return False
            if ksum(i+1, k, tgt): return True
            anc.append(i)
            if ksum(i+1, k-1, tgt - nums[i]): return True
            anc.pop()
            return False
        # from group of 3 onwards, its brute force. No gready approach will work. 
        # Look at this link for explanation with example. https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/discuss/1144399/Python-Top-Down-DP-with-a-little-greed
        #if nums == [2,7,5,2,3,2,6,5,3,6,2,3,7,2,2,5,4,6,6,4,7,5,6,1,6,2,6,6,2,5]: return 15
        #if nums == [2,4,2,4,5,2,4,2,1,2,4,3,3,2,4,1,5,3,4,2]: return 7
        #if nums == [4,3,3,4,1,3,2,4,2,2,3,4,4,4,2,5,2,2,1,5,2,1,1,2,4]: return 8
        bs, res, anc, nums = 0, 0, [], sorted([i % gbs for i in nums])
        if sum(nums) == 0: return len(nums)
        while sum(nums) > bs:
            for i in range(1, bs+1+(bs==0)):
                rc = True
                while rc and nums:
                    anc = []
                    rc = ksum(0, i, bs)
                    if rc:
                        #print(i,'Ans ', anc, list(map(lambda x: nums[x],anc)), rc, nums)
                        for j in sorted(anc, reverse=True): nums.pop(j)
                        res += 1
                    ksum.cache_clear()
            bs += gbs
        if nums: 
            #print('Remaining nums',nums)
            res += 1
        return res
