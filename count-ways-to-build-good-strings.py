class Solution:
    def countGoodStrings(self, low, high, zero, one):
        h, res=high+1, [0]*(high+1)
        res[0], m = 1, 1000000007
        for i in range(1, h):
            v1, v2 = (res[i-zero] if i >= zero else 0), (res[i-one] if i >= one else 0)
            res[i] = (v1 + v2) % m
        return sum(res[low:h]) % m
