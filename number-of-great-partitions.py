class Solution:
    def countPartitions(self, nums, k):
        sa = [0]*k
        sa[0] = 1
        for i in nums:
            nsa = list(sa) 
            for s in range(len(sa)):
                if s + i < k: 
                    nsa[s+i] += sa[s]
            sa = nsa
        #print('sum', sum(sa), sa)
        res = max(0, (2**len(nums) - 2*sum(sa)))
        return res % 1000000007
