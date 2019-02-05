# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = 0
        def dfs(r):
            global res
            if not r: return (0,0)
            c1,n1 = dfs(r.left)
            c2,n2 = dfs(r.right)
            N = n1 + n2 + r.val-1 # net coins going up
            res += c1 + c2
            #print r.val, 'L',(c1,n1), 'R',(c2,n2), 'E', c1+c2,N
            C = abs(N)
            return (C,N)
        dfs(root)
        return res
        
from library_for_lc import *
t = deser([0,0,0,0,0,0,7]) # 4
print Solution().distributeCoins(t) 
"""
t = deser([1,0,0,null,3]) # 4
print Solution().distributeCoins(t) 
t = deser([1,0,2]) # 2
print Solution().distributeCoins(t)
t = deser([0,3,0]) # 3
print Solution().distributeCoins(t)
t = deser([3,0,0]) # 2
print Solution().distributeCoins(t)
t = deser([1,3,1,0,0,0,2]) # 4
print Solution().distributeCoins(t)
"""
