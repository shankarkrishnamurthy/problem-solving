class Solution(object):
    def sufficientSubset(self, r, l):
        """
        :type r: TreeNode
        :type l: int
        :rtype: TreeNode
        """
        def dfs(r,v):
            if not r: return 0
            c = v+r.val
            if not r.left and not r.right:
                if c < l: return 0
                else: return 1

            a = dfs(r.left,c)
            b = dfs(r.right,c)
            #print 'r.val', r.val, 'c ',c,'a',a,'b',b
            if not a and not b: r.left = r.right = None
            elif not a: r.left = None
            elif not b: r.right = None
            else: pass
            return 1 if (r.left or r.right) else 0
        
        res = dfs(r,0)
        if not res: return None
        return r

from library_for_lc import *
t= deser([1,2,-3,-5,null,4,null])
print ser(Solution().sufficientSubset(t,-1))
t= deser([5,4,8,11,null,17,4,7,1,null,null,5,3])
print ser(Solution().sufficientSubset(t,22))
t= deser([1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14])
print ser(Solution().sufficientSubset(t,1))
