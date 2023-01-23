class Solution:
    def minOperations(self, nums1, nums2, k):
        tops, par = 0, 0
        if k == 0:
            if nums1 == nums2: return 0
            else: return -1
        for i,v in enumerate(nums1):
            d = v - nums2[i]
            q, r = divmod(d,k)
            if r != 0: return -1
            tops += abs(q)
            par += q
        if par != 0: return -1
        return tops>>1
