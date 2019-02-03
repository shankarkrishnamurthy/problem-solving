# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ha,res = {}, []
        def dfs(r, x, h, ha):
            if not r: return
            ha.setdefault(x, []).append((h,r.val))
            dfs(r.left, x-1, h+1, ha)
            dfs(r.right, x+1, h+1, ha)
            return
        dfs(root,0,0,ha)
        for k in sorted(ha):
            res.append([x[1] for x in sorted(ha[k])])
        return res

        
from library_for_lc import *
t = deser([1,2,3,4,5,6,7])
print Solution().verticalTraversal(t)
 
t = deser([3,9,20,null,null,15,7])
print Solution().verticalTraversal(t)
t = TreeNode(3)
t = deser([3])
print Solution().verticalTraversal(t)
