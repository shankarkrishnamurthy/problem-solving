class Solution:
    def singleNumber(self, nums):
        aXORb,n = 0,1
        for i in nums: aXORb ^= i
        while n <= 3001:
            if n & aXORb: break
            n = n << 1
        orig = aXORb
        for i in nums:
            if n & i: aXORb ^= i
        return [orig ^ aXORb, aXORb]

print(Solution().singleNumber([1,2,1,3,2,5]))
print(Solution().singleNumber([-1,0]))
print(Solution().singleNumber([1,0]))
