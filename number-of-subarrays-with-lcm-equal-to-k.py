class Solution:
    def subarrayLCM(self, nums, k):
        def gcd(a,b):
            if b==0: return a
            return gcd(b, a%b)
        res = 0
        for i in range(len(nums)):
            lcm = nums[i]
            for j in range(i,-1,-1):
                if k % nums[j]!= 0 or lcm > k: break
                cgcd = gcd(nums[j], lcm)
                lcm = lcm*nums[j]//cgcd
                if lcm == k: res += 1
                #print('i', i, (nums[i],nums[j]),'j', j, 'cgcd', cgcd, 'lcm',lcm, 'res', res)
        return res
