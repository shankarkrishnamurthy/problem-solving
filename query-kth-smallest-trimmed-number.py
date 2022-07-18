class Solution:
    def smallestTrimmedNumbers(self, nums, q):
        nh, n, res, ts = defaultdict(list), len(nums[0]), [], set()
        for (a,b) in q: ts.add(b)
        for i,v in enumerate(nums):
            for t in ts: nh[t].append((v[-t:], i))
        for t in nh: nh[t].sort()
        for (k, t) in q: res.append(nh[t][k-1][1])
        return res
