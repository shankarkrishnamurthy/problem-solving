class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        l,r = None,None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if l==None: l = i
            if nums[len(nums)-2-i] > nums[len(nums)-1-i]:
                if r==None: r = len(nums)-1-i
        if l == None: return 0
        mi,ma = min(nums[l:r+1]), max(nums[l:r+1])
        print(l,r,mi,ma)
        while l > 0 and mi < nums[l-1]: l-=1
        while r < len(nums)-1 and ma > nums[r+1]: r+=1
        print(nums,l,r)
        return r-l+1


print(Solution().findUnsortedSubarray([3,2,3,2,4]))
#print(Solution().findUnsortedSubarray([2]))
#print(Solution().findUnsortedSubarray([1,2]))
#print(Solution().findUnsortedSubarray([2,6,4,8,10,9,15]))
#print(Solution().findUnsortedSubarray([2,6,4,8,1,10,9,15]))
#print(Solution().findUnsortedSubarray([2,6,4,8,1,19,10,9,15]))
