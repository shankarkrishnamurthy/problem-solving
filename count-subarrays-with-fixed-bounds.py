class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res, l, miv, mav = 0, -1, None, None
        for i,v in enumerate(nums):
            if v > maxK or v < minK:
                l, miv, mav = i, None, None
            else:
                if v == minK: miv = i
                if v == maxK: mav = i
                if miv == None or mav == None: continue
                res += min(miv, mav) - l
        return res
