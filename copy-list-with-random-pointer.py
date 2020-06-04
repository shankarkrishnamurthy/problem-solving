# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

from typing import *
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        h, tmp = {}, head
        while tmp:
            #print(tmp,tmp.next,tmp.random)
            ntmp = Node(tmp.val,None, None)
            h[tmp] = ntmp
            tmp = tmp.next
        h[tmp] = tmp
        tmp = head
        while tmp:
            ntmp = h[tmp]
            ntmp.next = h[tmp.next]
            ntmp.random = h[tmp.random]
            tmp = tmp.next
        return h[head]

t = Node(2,None,None)
t1 = Node(1,t,t)
t.random = t
s = Solution().copyRandomList(t1)
while s:
    print(s,s.val) #,s.next,s.random)
    s = s.next
