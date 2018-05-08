class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        nums.insert(0,0)
        for i in range(1,len(nums)):
            if nums[i] < 0: continue
            j = nums[i]
            while nums[j] > 0:
                nums[j] *= -1
                j = -nums[j]
        for i in range(1,len(nums)):
            if nums[i] > 0: res.append(i)
        return res
                

print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
print Solution().findDisappearedNumbers([2,3,2])
print Solution().findDisappearedNumbers([1])
