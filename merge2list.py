# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from library_for_lc import *
class Solution:
    def mergeTwoLists(self, l1, l2):
        def addafter(c,l):
            cn = c.next
            c.next = l
            l.next = cn
            return l
        def disconnect(l2):
            d,l2 = l2, l2.next
            return d,l2
        if not (l1 and l2): return l2 or l1
        if l2.val < l1.val: l1,l2 = l2,l1
        h, l1 = disconnect(l1)
        i = h
        while l1 and l2:
            if l1.val < l2.val:
                d, l1 = disconnect(l1)
            else: 
                d, l2 = disconnect(l2)
            i = addafter(i,d)
        if l1 or l2: i.next = l1 or l2
        return h

print(prll(Solution().mergeTwoLists(arr2ll([]),arr2ll([]))))
print(prll(Solution().mergeTwoLists(arr2ll([]),arr2ll([0]))))
print(prll(Solution().mergeTwoLists(arr2ll([1]),arr2ll([]))))
print(prll(Solution().mergeTwoLists(arr2ll([1,2,4]),arr2ll([6,7,8]))))
print(prll(Solution().mergeTwoLists(arr2ll([10,12,14]),arr2ll([6,7,8]))))
print(prll(Solution().mergeTwoLists(arr2ll([1,2,4]),arr2ll([1,3,4]))))
print(prll(Solution().mergeTwoLists(arr2ll([1,2,4]),arr2ll([0,3,4]))))
