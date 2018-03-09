# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        q = [root]
        while True:
            tmp = []
            tres = []
            for v in q:
                tres.append(v.val)
                if v.left:
                    tmp.append(v.left)
                if v.right:
                    tmp.append(v.right)
            res += [tres]
            q = tmp
            if not tmp:
                return res

t1 = None
print Solution().levelOrder(t1)
t1 = TreeNode(3)
print Solution().levelOrder(t1)
t1.left = TreeNode(9)
print Solution().levelOrder(t1)
t1.right = TreeNode(20)
print Solution().levelOrder(t1)
t1.right.right = TreeNode(7)
print Solution().levelOrder(t1)
t1.right.left = TreeNode(15)
print Solution().levelOrder(t1)
t1.left.left = TreeNode(8)
print Solution().levelOrder(t1)

