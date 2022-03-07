class Solution:
    def maximumANDSum(self, nums, numSlots):
        st, msf  = [0]*(numSlots+1), 0

        #@lru_cache(None)
        def backtrack(k, res):
            nonlocal msf
            if k == len(nums):
                msf = max(msf, res)
                return 0
            for i in range(1, numSlots+1):
                if st[i] < 2:
                    val = i & nums[k]
                    st[i] += 1
                    backtrack(k+1, res + val)
                    st[i] -= 1
        backtrack(0, 0)
        return msf
        
#print(Solution().maximumANDSum([1,2,3,4,5,6], 3))
print(Solution().maximumANDSum([8,4,14,3,2,4,11,8,5,12,6,2],8))
