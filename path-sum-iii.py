# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        global res;
        def do_ps(root, anclist):
            global res;
            if not root: return
            # add current node to all nodes that came before it
            anclist += [0]
            for i in range(len(anclist)): 
                anclist[i] += root.val
                if anclist[i] == sum: res += 1
            print anclist
            # call child
            do_ps(root.left, anclist)
            do_ps(root.right, anclist)
            # remove current node from all nodes present
            for i in range(len(anclist)): 
                anclist[i] -= root.val
            anclist.pop(-1)    
            return

        res=0
        do_ps(root, [])
        return res

"""
t = TreeNode(10)
t.left = TreeNode(5)
t.left.right = TreeNode(2)
t.left.right.right = TreeNode(1)
t.left.left = TreeNode(3)
t.left.left.left = TreeNode(3)
t.right = TreeNode(-3)
t.right.right = TreeNode(11)
"""
#t = TreeNode(10)
#t = TreeNode(8)
t=None
print Solution().pathSum(t, 8)
