class Solution:
    def largestCombination(self, cand):
        bit={}
        for n in cand:
            while n:
                v = n & (n-1)
                bit[v^n] = bit.get(v^n, 0 ) + 1
                n = v
        #print(bit)
        res = max(bit.values())
        return res
