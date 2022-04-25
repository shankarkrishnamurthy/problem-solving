class Solution:
    def minOperations(self, nums: List[int]) -> int:
        msf, k, ns = len(nums), len(nums), list(set(nums))
        if k == 1: return 0
        dup, n = k - len(ns), len(ns)
        ns.sort()
        for i in range(n):
            j = bisect_left(ns, ns[i] + k)
            msf = min(msf, k - (j - i))
        return max(msf, dup)
