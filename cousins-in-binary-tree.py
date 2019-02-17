# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, r, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = set()
        q.add(r)
        while q:
            cur = set()
            v = set()
            p = {}
            for i in q:
                if i.left: 
                    cur.add(i.left)
                    v.add(i.left.val)
                    p[i.left.val] = i
                if i.right: 
                    cur.add(i.right)
                    v.add(i.right.val)
                    p[i.right.val] = i
            if v and x in v and y in v and p[x] != p[y]: return True
            if not cur: break
            q = cur

        return False

from library_for_lc import *
#t=deser([1,2,3,4])
#print Solution().isCousins(t, 4, 3)
#t = deser([1,2,3,null,4,null,5])
#print Solution().isCousins(t, 5, 4)
#t=deser([1,2,3,null,4])
#print Solution().isCousins(t, 4, 3)
t=deser([1,2,3,null,4])
print Solution().isCousins(t, 2, 3)
#t=deser([1,2,3])
#print Solution().isCousins(t, 2, 3)

