from library_for_lc import *
from bisect import *
class Solution(object):
    def bstFromPreorder(self, pre):
        """
        :type pre: List[int]
        :rtype: TreeNode
        """
        if not pre: return None
        c = TreeNode(pre[0])
        if len(pre) == 1 : return c
        i = bisect_left(pre,c.val)
        if i==0: i += 1
        #print pre, c.val, i
        c.left = self.bstFromPreorder(pre[1:i])
        c.right = self.bstFromPreorder(pre[i:])
        return c

t = Solution().bstFromPreorder([8,5,1,7,10,12])
print ser(t)
t = Solution().bstFromPreorder([8])
print ser(t)
t = Solution().bstFromPreorder([8,1])
print ser(t)
t = Solution().bstFromPreorder([8,12])
print ser(t)
