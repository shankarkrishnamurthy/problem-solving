class Solution:
    def maximumANDSum(self, nums, numSlots):
        st  = [0]*(numSlots+1)

        @lru_cache(None)
        def backtrack(k, stt):
            if k == len(nums): return 0
            rc,st = 0,list(stt)
            for i in range(1, numSlots+1):
                if st[i] < 2:
                    val = i & nums[k]
                    st[i] += 1
                    val +=backtrack(k+1, tuple(st))
                    rc = max(rc, val)
                    st[i] -= 1
            return rc
        return backtrack(0, tuple(st))
        
