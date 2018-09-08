# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leafs(r):
            if not r:
                return []
            if not r.left and not r.right:
                return [r.val]
            return get_leafs(r.left) + get_leafs(r.right)
            
        def leaf_simi(n1,n2):
            return n1==n2
        
        n1 = get_leafs(root1)
        n2 = get_leafs(root2)
        if leaf_simi(n1,n2):
            return True
        else:
            return False

t1=TreeNode(3)
t1.left=TreeNode(5)
t1.right=TreeNode(1)
t2=TreeNode(4)
t2.left=TreeNode(5)
t2.right=TreeNode(1)
print Solution().leafSimilar(t1,t2)
t1=TreeNode(4)
t2=TreeNode(4)
print Solution().leafSimilar(t1,t2)
t1=TreeNode(1)
t2=TreeNode(4)
print Solution().leafSimilar(t1,t2)
