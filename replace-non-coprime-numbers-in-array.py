class Solution:
    def replaceNonCoprimes(self, nums):
        def gcd(a,b):
            if b==0: return a
            return gcd(b, a%b)
        res = [nums[0]]
        for i in range(1,len(nums)):
            v = nums[i]
            cp = gcd(res[-1], v)
            while res and cp > 1:
                lv = res.pop()
                nv = v*lv//cp
                if res: cp = gcd(res[-1], nv)
                v = nv
            res.append(v)
        return res
