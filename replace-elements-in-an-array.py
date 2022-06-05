class Solution:
    def arrayChange(self, nums, ops):
        ih = {v:i for i,v in enumerate(nums)}
        for (old,new) in ops:
            i = ih[old]
            del ih[old]
            nums[i] = new
            ih[new] = i
        return nums
            
        
