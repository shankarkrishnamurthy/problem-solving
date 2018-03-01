# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findPath(self, root, n, nPath)
        nPath.append(root);
        if (root == n):
            return nPath
        
        if root.left:
            l = self.findPath(self, root.left, n, nPath)
        if not l and root.right:
            r = self.findPath(self, root.right, n, nPath)
    
        nPath.pop(-1);
        return nPath
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pPath = []
        qPath = []
        self.findPath(root,p, pPath);
        self.findPath(root,q, qPath);

        for i,j in zip(pPath, qPath):
            if i == j:
                ans = j;
                continue;
            break;

        return ans


