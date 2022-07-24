class Solution:
    def zeroFilledSubarray(self, nums):
        res, l = 0, -1
        for i,v in enumerate(nums):
            if v != 0: 
                l = -1
                continue
            if l == -1: l, res = i, res+1
            else: res += i - l + 1
        return res
        
