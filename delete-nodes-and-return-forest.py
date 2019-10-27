# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from library_for_lc import *
from typing import *
class Solution:
    def __init__(self):
        self.ans = []
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(ro):
            if not ro: return None
            l = dfs(ro.left)
            r = dfs(ro.right)
            if ro.val in ds:
                if l: self.ans.append(l)
                if r: self.ans.append(r)
                return None
            ro.left = l
            ro.right= r
            return ro
        ds = set(to_delete)
        rc = dfs(root)
        if rc: self.ans.append(rc)
        return self.ans
            
a =Solution().delNodes(deser([1,2,3,4,5,6,7]), [3,5])
for i in a: print(ser(i))
a =Solution().delNodes(deser([1,2]), [1])
for i in a: print(ser(i))
