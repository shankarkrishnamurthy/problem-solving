class Solution:
    def maxScore(self, nums1, nums2, k):
        hq, res, ts = [], 0, 0
        for s,m in sorted(zip(nums1,nums2), key=lambda x: -x[1]):
            heappush(hq, s)
            ts += s
            if len(hq) > k:
                ts -= heappop(hq)
            if len(hq) == k:
                res = max(res, m*ts)
        return res
