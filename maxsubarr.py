class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mend = nums[0]
        mall = mend
        sh = eh = 0
        for idx in range(1,len(nums)):
            i = nums[idx]
            mend = max(i + mend, i)
            if i == mend:
                s = idx
            
            if mall < max(mend, mall):
                eh = idx
                sh = s
                mall = max(mend, mall)
        return (mall, sh, eh)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mend = nums[0]
        mall = mend
        for idx in range(1,len(nums)):
            i = nums[idx]
            mend = max(i + mend, i)
            mall = max(mend, mall)
        return mall


print Solution().maxSubArray([-2])
print Solution().maxSubArray([1,-2])
print Solution().maxSubArray([-3,1])
print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
