class Solution:
    def xorAllNums(self, nums1, nums2):
        n, m, xor1, xor2 = len(nums1), len(nums2), 0, 0
        for i in nums1: xor1 ^= i
        for i in nums2: xor2 ^= i
        if n%2 and m%2: return xor1 ^ xor2
        elif n%2: return xor2
        elif m%2: return xor1
        else: return 0
