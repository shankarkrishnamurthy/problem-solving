class Solution:
    def maximumsSplicedArray(self, nums1, nums2):
        def msa(nums):
            mend = nums[0]
            mall = mend
            for idx in range(1,len(nums)):
                i = nums[idx]
                mend = max(i + mend, i)
                mall = max(mend, mall)
            #print('nl', nl, 'msa', mall)
            return mall
        nl, s1, s2 = [], sum(nums1), sum(nums2)
        for i,j in zip(nums1,nums2): nl.append(i-j)
        b, d = s2, msa(nl)
        res1, nl = b + (d if d > 0 else 0), []
        for i,j in zip(nums2,nums1): nl.append(i-j)
        b, d = s1, msa(nl)
        res2 = b + (d if d > 0 else 0)
        #print('res1', res1, 'res2',  res2)
        return max(res1, res2)
