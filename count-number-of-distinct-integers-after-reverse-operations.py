class Solution:
    def countDistinctIntegers(self, nums):
        nh = set(nums)
        for i in nh:
            nums.append(int(str(i)[::-1]))
        return len(set(nums))
        
