from bisect import bisect_left as bl
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print nums,": ", 
        if len(nums) == 0: return []
        if len(nums) == 1: return [0]
        res=[]
        ans=[]
        for v in nums[::-1]:
            if not res:
                res.append(v)
                ans.append(0)
                continue
            idx = bl(res, v)
            res[idx:idx] = [v]
            ans.append(idx)
        return ans[::-1]

print Solution().countSmaller([5,6,2,1])
print Solution().countSmaller([2,1])
print Solution().countSmaller([1,2])
print Solution().countSmaller([2,1,2])
