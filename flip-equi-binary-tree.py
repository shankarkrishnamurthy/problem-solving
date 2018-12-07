# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, r1, r2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        if r1.val != r2.val: 
            print 'Failed ',r1.val, r2.val
            return False
        if not r1.left and not r1.right and not r2.left and not r2.right: return True
        print r1.val, r2.val

        rc = False
        if (r1.left and r2.left and r1.left.val == r2.left.val) or (r1.right and r2.right and r1.right.val == r2.right.val): 
                rc = self.flipEquiv(r1.left,r2.left) and self.flipEquiv(r1.right, r2.right)
        elif (r1.left and r2.right and r1.left.val == r2.right.val) or (r1.right and r2.left and r1.right.val == r2.left.val):
                rc = self.flipEquiv(r1.left, r2.right) and self.flipEquiv(r1.right, r2.left)

        return rc

t1 = TreeNode(0)
t1.left = TreeNode(3)
t1.right = TreeNode(1)
t1.right.right = TreeNode(2)
t2 = TreeNode(0)
t2.left = TreeNode(3)
t2.right = TreeNode(1)
t2.left.left = TreeNode(2)
print '******'
print Solution().flipEquiv(t1,t2)

t1 = TreeNode(0)
t1.left = TreeNode(3)
t1.right = TreeNode(1)
t2 = TreeNode(0)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
print '******'
print Solution().flipEquiv(t1,t2)


t1 = TreeNode(0)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t2 = TreeNode(0)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
print '******'
print Solution().flipEquiv(t1,t2)

