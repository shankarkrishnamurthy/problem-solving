# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.stackstore=[]        

    def is_leaf(self, root):
        return (root.left == None and root.right == None)

    def binaryTreePathsWithAnc(self, root, ancestry):
        if self.is_leaf(root):
            return [root.val]

        ancestry.append(str(root.val))
        lstrlist = rstrlist = []
        if (root.left != None):
            lstrlist = self.binaryTreePathsWithAnc(root.left, ancestry)

        if (root.right != None):
            rstrlist = self.binaryTreePathsWithAnc(root.right, ancestry)

        mlist = []
        for x in lstrlist,rstrlist:
             mlist.append('->'.join(ancestry) + '->' + str(x))

        ancestry.pop(-1)
        return mlist

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.binaryTreePathsWithAnc(root, [])

t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(7)
t1.left.right = TreeNode(9)
t1.left.left = TreeNode(1)
s = Solution()
slist = s.binaryTreePaths(t1)
print slist
