# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from library_for_lc import *
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def find(r):
            if not r: return None
            if r.val == x: return r
            a = find(r.left)
            b = find(r.right)
            return a or b
        def cnt(r):
            if not r: return 0
            return cnt(r.left) + cnt(r.right) + 1

        r = find(root)
        c1 = cnt(r.left)
        c2 = cnt(r.right)
        p = n - c1 - c2 - 1
        print (c1, c2 , p)
        if p > c1 + c2 +1 or c1 > p + c2 + 1 or c2 > p + c1 + 1: return True
        return False
        
t = deser([1,2,3,4,5,6,7,8,9,10,11])
print(Solution().btreeGameWinningMove(t,11,3))
