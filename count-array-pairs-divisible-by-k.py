class Solution:
    def countPairs(self, nums, k):
        def gcd(a,b):
            if b==0: return a
            return gcd(b,a%b)
        gh, res, cgl = {}, 0, []
        for v in nums:
            cg = gcd(v, k)
            cgl.append(cg)
            gh[cg] = gh.get(cg, 0) + 1
        for i,v in enumerate(nums):
            nv= k//cgl[i]
            cr = sum([gh[x] for x in gh if x%nv==0])
            if cgl[i] % nv == 0: cr -= 1
            #print('i,v', i,v, 'gcd', cgl[i], 'neededgcdlist', [(x,gh[x]) for x in cgl if x%nv == 0], 'curr', cr)
            res += cr
        return res//2
