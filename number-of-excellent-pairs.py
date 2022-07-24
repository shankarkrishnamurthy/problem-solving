class Solution:
    def countExcellentPairs(self, nums, k):
        def count(n):
            c = 0
            while n:
                n = n & (n-1)
                c += 1
            return c
        ns, nb, res = set(), [0]*32, 0
        for i in nums:
            if i in ns:  continue #dup
            ns.add(i)
            nb[count(i)] += 1
        #print('nb', nb)
        for i in range(1,len(nb)):
            for j in range(1,len(nb)):
                if i + j < k: continue
                res += nb[j]*nb[i]
        return res
