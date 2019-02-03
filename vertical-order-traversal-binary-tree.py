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
        
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)
print Solution().verticalTraversal(t)
 
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print Solution().verticalTraversal(t)
t = TreeNode(3)
print Solution().verticalTraversal(t)
