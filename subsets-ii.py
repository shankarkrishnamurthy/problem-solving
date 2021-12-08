class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        out=[[]]
        for i,v in enumerate(nums):
            if i and v == nums[i-1]:
                p = [ c + [v] for c in p ]
            else:
                p = [ c + [v] for c in out ] 
            out += p
        return out

print(Solution().subsetsWithDup([0]))
print(Solution().subsetsWithDup([1,2,2]))
print(Solution().subsetsWithDup([2,2]))
