class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        comple,cntres, sumsf = {0: 1},0,0
        for i in range(len(nums)):
            sumsf += nums[i]
            if comple.has_key(sumsf - k):
                cntres += comple.get(sumsf-k,0)
            comple[sumsf] = comple.get(sumsf,0) + 1
            print comple
        return cntres
            

#print Solution().subarraySum([1,1,1],2)
#print Solution().subarraySum([1,2,3],3)
print Solution().subarraySum([0,1,0,0,1],1)
#print Solution().subarraySum([-1,0,1],0)
