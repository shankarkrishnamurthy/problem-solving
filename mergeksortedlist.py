# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    @staticmethod
    def println(ln):
        print('['),
        while ln:
            print ln.val, 
            ln = ln.next
        print(']')

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if k == 0: return None
        if k == 1: return lists[0]
        head, tail,=None, None
        idxset = set([i for i in range(0,k) if lists[i]])
        k=len(idxset)
        if k == 0: return None
        if k == 1: return lists[list(set(idxset))[0]]
        while len(idxset) > 1:
            mval = float("inf")
            for i in idxset:
                v = lists[i]
                if v.val < mval:
                    mval = v.val
                    mi = i
            if not head:
                head = lists[mi]
                tail = head
            else:
                tail.next = lists[mi]
                tail = tail.next
            lists[mi] = lists[mi].next
            tail.next = None
            if not lists[mi]:
                idxset.remove(mi)
        tail.next = lists[list(set(idxset))[0]]
        return head
        
l1 = ListNode(4)
l1.next = ListNode(5)
l2 = ListNode(2)
l3 = ListNode(6)
l4 = None
l5 = ListNode(8)
ListNode.println(Solution().mergeKLists([l1,l2,l3,l4,l5]))
ListNode.println(Solution().mergeKLists([None,None]))
ListNode.println(Solution().mergeKLists([None,l5]))
