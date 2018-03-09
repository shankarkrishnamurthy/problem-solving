class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0: return 1
        for i,v in enumerate(nums):
            if v < 1 or v > l: 
                nums[i] = 0
        #print nums, l
        busy = -(l+1)
        for i,v in enumerate(nums):
            if v == 0 : continue
            cbusy = False
            if v < 0 : 
                nums[i] = busy
                v = -v
                if v > l: continue
                cbusy = True
            if v-1 <= i:
                nums[v-1] = busy
            else:
                if nums[v-1] >= 0:
                    nums[v-1] = -nums[v-1] if nums[v-1] != 0 else busy
            if not cbusy and i != v-1:
                nums[i] = 0
        #print i, nums
        for i,v in enumerate(nums):
            if v == 0:
                return i+1
        return l+1
 
print Solution().firstMissingPositive([43,20,39,-7,-8,-2,8,17,10,17,12,6,37,17,50,44,3,11,18,-4,44,37,28,50,15,50,19,0,45,5,37,35,35,21,39,35,27,-8,-1,47,19,22,1,1,47,-4,-7,-3,16,21,2,7,6])
print Solution().firstMissingPositive([3,4,0,2])
print Solution().firstMissingPositive([3,4,-1,1])
print Solution().firstMissingPositive([0,1])
print Solution().firstMissingPositive([])
print Solution().firstMissingPositive([0])
print Solution().firstMissingPositive([1])
print Solution().firstMissingPositive([2])
print Solution().firstMissingPositive([0,-1])
print Solution().firstMissingPositive([1,0])
print Solution().firstMissingPositive([1,2])
print Solution().firstMissingPositive([2,1])
print Solution().firstMissingPositive([3,2,1])
print Solution().firstMissingPositive([3,0,1])
print Solution().firstMissingPositive([3,2,1,0])
