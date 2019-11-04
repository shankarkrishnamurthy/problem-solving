from typing import *
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        st = []
        for i,v in enumerate(nums):
            if v % 2 == 1: st.append(i)
        #print(st)
        ans = 0
        for i in range(k-1,len(st)):
            (li,lo) = (st[i-k],st[i-k+1]) if i-k>=0 else (-1,st[0])
            (ri,ro) = (st[i+1],st[i]) if i != len(st)-1 else (len(nums),st[-1])
            ans += (lo-li)*(ri-ro)
            #print(li,lo, ro,ri, (lo-li)*(ri-ro) )
        return ans
        
print(Solution().numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
print(Solution().numberOfSubarrays(nums = [3], k = 1))
print(Solution().numberOfSubarrays(nums = [3,5], k = 2))
print(Solution().numberOfSubarrays(nums = [2,3,5], k = 2))
print(Solution().numberOfSubarrays(nums = [2,3,5,4], k = 2))
print(Solution().numberOfSubarrays(nums = [2,3,6,5,4], k = 2))
print(Solution().numberOfSubarrays(nums = [2,4,6], k = 1))
print(Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
