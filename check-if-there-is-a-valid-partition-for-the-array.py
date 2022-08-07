class Solution:
    def validPartition(self, nums):
        n=len(nums)
        @lru_cache(None)
        def dfs(i):
            if i == n: return True
            if i == n-1: return False
            v1, v2 = False, False
            if i+1 < n and nums[i] == nums[i+1]: v1 = dfs(i+2)
            if not v1 and i+2 < n and ((nums[i] == nums[i+1] == nums[i+2]) \
                or (nums[i] == nums[i+1]-1 == nums[i+2]-2)): 
                v2 = dfs(i+3)
            #print('i', i, v1, v2)
            return v1 or v2
        return dfs(0)
