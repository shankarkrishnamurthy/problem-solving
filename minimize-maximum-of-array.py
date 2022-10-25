class Solution:
    def minimizeArrayValue(self, nums):
        def canReduce(mmv):
            co = 0
            for i in range(len(nums)-1,-1,-1):
                cco = co + nums[i] - mmv
                if cco <= 0: co = 0
                else: co = cco
            return co == 0
        l, r = 0, max(nums)
        while l < r:
            m = (l + r) // 2
            rc = canReduce(m)
            #print('For Max Val', m,l,r, "canReduce rc", rc)
            if rc: r = m
            else: l = m + 1
        return l
