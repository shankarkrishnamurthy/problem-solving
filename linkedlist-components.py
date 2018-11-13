# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        g = set(G)
        tmp = head
        res,f = 0,False
        while tmp:
            if tmp.val not in g:
                if f: res += 1
                f = False
            else:
                f = True
            tmp = tmp.next
        if f: res += 1
        return res

t = ListNode(0)
t.next = ListNode(1)
t.next.next = ListNode(2)
t.next.next.next = ListNode(3)
print Solution().numComponents(t, [0,1,3])
print Solution().numComponents(t, [0,1])
t = ListNode(0)
t.next = ListNode(1)
t.next.next = ListNode(2)
t.next.next.next = ListNode(3)
t.next.next.next.next = ListNode(4)
print Solution().numComponents(t, [0,3,1,4])
