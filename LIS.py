from bisect import bisect_left as bl
class Solution(object):
    def lengthOfLIS(self, nums):
        a = []
        for i in nums:
            if not a or a[-1]<i:
                a.append(i)
            else:
                m = bl(a,i)
                a[m] = i
            
        return len(a)
            
print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
