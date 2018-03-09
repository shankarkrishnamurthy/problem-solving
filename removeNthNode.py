# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None
    @staticmethod
    def printll(ln):
        print "[",
        while ln:
            print ln.val,
            ln=ln.next
        print "]"

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr, i = head, n
        if not head: return None
        if not head.next: return None
        while i and ptr:
            i -= 1
            ptr=ptr.next
        if not ptr: 
            return head.next
        pre, rnode = None, head
        while ptr:
            pre=rnode
            rnode = rnode.next
            ptr = ptr.next
        pre.next = rnode.next
        return head

l1 = ListNode(1)
p=Solution().removeNthFromEnd(l1,1)
ListNode.printll(p)
l1 = ListNode(2)
l1.next = ListNode(4)
p=Solution().removeNthFromEnd(l1,1)
ListNode.printll(p)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(6)
l1.next.next.next = ListNode(8)
p=Solution().removeNthFromEnd(l1,4)
ListNode.printll(p)
