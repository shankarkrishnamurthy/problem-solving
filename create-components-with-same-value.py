class Solution:
    def componentValue(self, nums, edges):
        def dfs(r, vis, tot):
            tv = nums[r]
            vis.add(r)
            for e in g[r]:
                if e in vis: continue
                ch = dfs(e, vis, tot)
                if ch < 0: return -1
                tv += ch
            if  tv > tot: return -1
            return tv % tot
        g, vis, suv = defaultdict(list), set(), sum(nums)
        for i,j in edges: _, __ = g[i].append(j), g[j].append(i)
        f = [ i for i in range(1, suv + 1) if suv % i == 0 ]
        for e in f:
            if dfs(0, set(), e) == 0: return suv//e-1
        
