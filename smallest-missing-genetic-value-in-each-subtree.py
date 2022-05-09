class Solution:
    def smallestMissingValueSubtree(self, pa, nums):
        nc, res= [[] for i in range(len(pa))], [1]*(len(pa))
        for i in range(1, len(pa)):
            nc[pa[i]].append(i)
        vis, mi = set(), 2
        def dfs(r):
            if nums[r] in vis: return
            for c in nc[r]: 
                dfs(c)
            vis.add(nums[r])
        try: i = nums.index(1)
        except: i = -1
        while i != -1:
            dfs(i)
            while mi in vis: mi += 1
            res[i] = mi
            i = pa[i]
        return res
            
