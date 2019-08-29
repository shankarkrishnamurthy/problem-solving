# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from library_for_lc import *
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def dn(p,a,b,h,s):
            t = p.next
            p.next = b.next
            while t and t != b.next:
                s += t.val
                t = t.next
                del h[s]
            h[s] = p
            return p

        t,s = head,0
        while t:
            s+= t.val
            t = t.next
            if s == 0: head = t
        if head: 
            h,s,tp = {0: head},0,head
            while tp:
                #print tp.val, s
                s+= tp.val
                if s in h:
                    par = dn(h[s],h[s].next, tp,h,s)
                    tp = par.next
                    continue
                h[s] = tp
                par = tp
                tp = par.next
        print prll(head)
        return head
            
Solution().removeZeroSumSublists(arr2ll([1,3,2,-3,-2,5,5,-5,1]))
Solution().removeZeroSumSublists(arr2ll([0,0,1]))
Solution().removeZeroSumSublists(arr2ll([1,2,-3,3,1]))
Solution().removeZeroSumSublists(arr2ll([1,2,3,-3,4]))
Solution().removeZeroSumSublists(arr2ll([1,2,3,-3,-2]))
Solution().removeZeroSumSublists(arr2ll([0]))
Solution().removeZeroSumSublists(arr2ll([-2,0,2]))
Solution().removeZeroSumSublists(arr2ll([-1,-2,0,-1,2,2,-1,1]))
