# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from library_for_lc import *

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res,st,c =[],[],0
        while head:
            #print 'val ', head.val
            res.append(0)
            v = head.val
            while st:
                m,n = st[-1]
                if n < v:
                    m,n = st.pop()
                    res[m] = v
                else:
                    break
            st.append((c,v))
            head = head.next
            c+=1
        return res
            
print Solution().nextLargerNodes(arr2ll([2,1,5]))
print Solution().nextLargerNodes(arr2ll([2,7,4,3,5]))
print Solution().nextLargerNodes(arr2ll([1,7,5,1,9,2,5,1]))
