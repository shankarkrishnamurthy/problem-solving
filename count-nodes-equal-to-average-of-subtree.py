class Solution:
    def averageOfSubtree(self, root):
        res = 0
        def dfs(r):
            nonlocal res
            if not r: return (0,0)
            
            s1, n1 = dfs(r.left)
            s2, n2 = dfs(r.right)
            
            s, n = s1+s2+r.val, n1 + n2 + 1
            if r.val == s//n: res += 1
            return (s,n)
            
        dfs(root)
        return res
