from typing import *
class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        h,msf = {},0
        for i in arr:
            h[i] = h.get(i-d,0)+1
            msf = max(msf, h[i])
        return msf

print(Solution().longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], d = -2))
print(Solution().longestSubsequence(arr = [1,3,5,7], d = 1))
print(Solution().longestSubsequence(arr = [1,2,3,4], d = 1))
