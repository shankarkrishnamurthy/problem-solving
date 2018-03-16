# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        head, tail = None, None
        while l1 and l2:
            if l1.val < l2.val :
                t=l1
                l1 = l1.next
            else:
                t=l2
                l2=l2.next
            if not head:
                head, tail = t, t
                t.next=None
                continue
            tail.next = t
            tail = t
            tail.next = None
        if not l1:
            tail.next = l2
        else:
            tail.next = l1
        return head

l1=ListNode(1)
l1.next = ListNode(4)
l2=ListNode(2)
l2.next=ListNode(3)
l2.next.next=ListNode(5)
l= Solution().mergeTwoLists(l1,l2)
print "[",
while l:
    print l.val,
    l = l.next
print "]"
