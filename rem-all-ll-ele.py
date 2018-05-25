# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        ptr = head
        while ptr and ptr.val == val: ptr = ptr.next
        head = ptr
        while ptr: # ptr.val != val
            nptr = ptr.next
            while nptr and nptr.val == val: nptr = nptr.next
            ptr.next = nptr
            ptr = nptr
        return head

ll = ListNode(3)
ll.next = ListNode(3)
ll.next.next = ListNode(2)
print Solution().removeElements(ll,3)
