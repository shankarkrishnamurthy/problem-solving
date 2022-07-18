class Solution:
    def minOperations(self, nums, nd):
        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a%b)
        v, res, l = nd[0], 0, 0
        for i in range(1, len(nd)):
            v = gcd(v, nd[i])
        nums.sort()
        for x in nums:
            if x > v: return -1
            if v % x == 0: return res
            res += 1
        return -1
