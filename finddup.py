class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3: return nums[0]
        L, R = 1, l
        while True:
            mid = (L + R) / 2
            lt = 0
            for v in nums:
                lt += 1 if v <= mid else 0
            if lt > mid:
                R = mid
            else:
                L = mid + 1
            if L == R:
                return L

print Solution().findDuplicate([1,2,2])
print Solution().findDuplicate([4,1,2,3,1])
print Solution().findDuplicate([4,4,4,1,2,3])
print Solution().findDuplicate([1])
print Solution().findDuplicate([1,1])
