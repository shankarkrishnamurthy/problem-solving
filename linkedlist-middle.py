# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p,n = head, head
        while n:
            n = n.next
            if not n: return p
            else: n = n.next
            p = p.next
            if not n: return p

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
#l.next.next.next = ListNode(4)
#l.next.next.next.next = ListNode(5)
print Solution().middleNode(l).val
