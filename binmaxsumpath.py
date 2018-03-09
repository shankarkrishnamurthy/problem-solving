# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.msf = float("-inf")
    def maxPathSum(self, root):
        def do_maxPathSum(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if not root:
                return 0
            ml = do_maxPathSum(root.left)
            mr = do_maxPathSum(root.right)
            maxsingle = max(ml+root.val, mr+root.val, root.val)
            self.msf = max(self.msf, maxsingle,  ml + root.val + mr)
            print maxsingle, ml, mr, root.val, self.msf
            return maxsingle
        do_maxPathSum(root)
        return self.msf

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t2 = TreeNode(3)
t2.left = t1
print Solution().maxPathSum(t1)
print Solution().maxPathSum(t2)
