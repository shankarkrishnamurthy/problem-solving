class Solution:
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        l, r, psf, nsf = 0, 0, 1, 0
        while r  < len(nums):
            psf *= nums[r]
            while l <= r and not psf < k:
                psf /= nums[l]
                l += 1
            if not l > r: nsf += r-l+1
            r += 1
        return nsf

print(Solution().numSubarrayProductLessThanK([10,5,2,6], 100))
print(Solution().numSubarrayProductLessThanK([1,2,3], 0))
        
