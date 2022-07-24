class Solution:
    def minCameraCover(self, root):
        def dfs(r):
            nonlocal tot
            if not r: return 1
            rl, rr = dfs(r.left), dfs(r.right)
            if rl == 0 or rr == 0: 
                tot+=1
                return 2
            if rl == 2 or rr == 2: return 1
            if rl == 1 and rr == 1: return 0

        tot = 0
        res = dfs(root)
        #print('ROOT', res, 'TOT', tot)
        return tot if res != 0 else 1+tot
