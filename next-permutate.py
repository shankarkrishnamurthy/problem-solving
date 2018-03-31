class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)==1: return
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]: 
                rep = i+1
                for j in range(rep+1, len(nums)):
                    if nums[j] > nums[i] and nums[j] < nums[rep]: rep = j
                nums[i] , nums[rep] = nums[rep], nums[i]
                sl = sorted(nums[i+1:])
                for j in range(i+1,len(nums)):
                    nums[j] = sl[j-i-1]
                return
        nums.reverse()
            
#n = [1,2,3]
#n = [2,3,4,1]
#n = [2,4,1,0,0]
#n=[1]
#n=[1,2]
#n=[1,1,5]
#n=[3,2,1]
#n = [2,3,5,4]
n = [1,3,2]
Solution().nextPermutation(n)
print n
#print Solution().nextPermutation([1,1,5])
