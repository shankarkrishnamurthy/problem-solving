# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from library_for_lc import *
import re

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        def dfs(r,h):
            while self.i < len(self.m):
                l,n = len(self.m[self.i][0]), None
                while h+1 == l:
                    n = TreeNode(int(self.m[self.i][1]))
                    if r.left: r.right = n
                    else: r.left = n
                    self.i += 1
                    l = len(self.m[self.i][0]) if self.i < len(self.m) else 0
                if n and l > h+1: 
                    dfs(n, h+1)
                if l < h+1: return
            return

        self.m = re.findall(r"(-*)(\d+)",S)
        #if self.m: print self.m
        self.i = 1
        r = TreeNode(int(self.m[0][1]))
        dfs(r,0)
        return r

s = Solution().recoverFromPreorder("1-2--3--4-5--6--7")
print ser(s)
s = Solution().recoverFromPreorder("1-2--3---4-5--6---7")
print ser(s)
s = Solution().recoverFromPreorder("1-401--349---90--88")
print ser(s)
s = Solution().recoverFromPreorder("1")
print ser(s)
