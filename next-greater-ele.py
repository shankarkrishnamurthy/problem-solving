class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res,n2h =[], {v:i for i,v in enumerate(nums)}
        for i in findNums:
            k = n2h[i]
            done = False
            for j in range(k+1,len(nums)):
                if nums[j] > i: 
                    res.append(nums[j])
                    done = True
                    break
            if not done: res.append(-1)
        return res

print Solution().nextGreaterElement([2,4],[1,2,3,4])
print Solution().nextGreaterElement([4,1,2],[1,3,4,2])
