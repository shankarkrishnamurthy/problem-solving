class Solution:
    def countDistinct(self, nums, k, p):
        res = set()
        for i in range(len(nums)):
            a = 0
            for j in range(i, -1,-1):
                if nums[j] % p == 0: a += 1
                if a > k: break
                res.add(tuple(nums[j:i+1]))
        #print(res)
        return len(res)
        
