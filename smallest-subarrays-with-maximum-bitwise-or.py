class Solution:
    def smallestSubarrays(self, nums):
        n, bh = len(nums), defaultdict(int)
        res, r, bv = [0]*n, n-1, [[] for _ in range(n)]
        
        for i in range(len(nums)-1,-1,-1):
            v = nums[i]
            while v:
                x = v & ~(v-1)
                bh[x] += 1
                bv[i].append(x)
                v = v & ~x
            while i < r:
                if not all([bh[j] > 1 for j in bv[r]]): break
                for j in bv[r]: bh[j] -= 1
                r -= 1
            #print('i', i, 'r', r, 'bh', dict(bh))
            res[i] = (r-i+1)
        return res
        
