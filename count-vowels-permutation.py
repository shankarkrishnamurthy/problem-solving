class Solution:
    def countVowelPermutation(self, n):
        vl, m = [1,1,1,1,1], 1000000007
        for i in range(1,n):
            nvl = [0]*5
            nvl[0] = vl[1] + vl[2] + vl[4]
            nvl[1] = vl[0] + vl[2]
            nvl[2] = vl[1] + vl[3]
            nvl[3] = vl[2]
            nvl[4] = vl[2] + vl[3]
            vl = nvl
        return sum(vl) % m
