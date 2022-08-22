class Solution:
    def kSum(self, nums, k):
        m = sum(x for x in nums if x > 0)
        pq = [(-m, 0)] 
        vals = sorted(abs(x) for x in nums)
        for _ in range(k): 
            x, i = heappop(pq)
            if i < len(vals): 
                heappush(pq, (x+vals[i], i+1))
                if i: heappush(pq, (x-vals[i-1]+vals[i], i+1))
        return -x
