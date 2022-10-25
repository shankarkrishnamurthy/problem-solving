class Solution:
    def maxDotProduct(self, nums1, nums2):
        @lru_cache(None)
        def walk(i, j):
            if i>= len(nums1) or j >=len(nums2): 
                return float("-inf")
            v1, v2, v3 = walk(i+1, j), walk(i,j+1), walk(i+1,j+1)
            val = nums1[i]*nums2[j]
            if  v3 != float("-inf"):
                val += v3
            #print('i',i,'j',j, max(v1,v2,v3) )
            return max(v1,v2,val)
        return walk(0,0)
