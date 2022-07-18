class Solution:
    def subarraysWithKDistinct(self, nums,k):
        n, lke, rke, l, r, res = len(nums), defaultdict(int), defaultdict(int), 0, 0, 0
        for j in range(n):
            lke[nums[j]], rke[nums[j]]= lke[nums[j]]+1, rke[nums[j]]+1
            if len(lke) < k: continue
            while len(lke) > k:
                if lke[nums[l]] == 1: del lke[nums[l]]
                else: lke[nums[l]] -= 1
                l += 1
            while len(rke) > k-1:
                if len(rke) == k and rke[nums[r]] == 1: break
                if rke[nums[r]] == 1: del rke[nums[r]]
                else: rke[nums[r]] -= 1
                r += 1
            res += r - l + 1
            #print('End j', j, 'L', l, 'R', r, 'lke', dict(lke), 'rke', dict(rke), 'res', res)
        return res
