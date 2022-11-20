class Solution:
    def subarrayGCD(self, nums, k):
        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a%b)
        res = 0
        for i, v in enumerate(nums):
            px = v
            for j in range(i,-1,-1):
                px = gcd(px,nums[j])
                if px % k != 0: break
                if px == k: res += 1
                #print(i,j, px, res)
        return res
