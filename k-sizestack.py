#
#  Description: This data structure drops the elements 
#               when stack gets more than k-size
#               The element getting dropped follows FIFO (ironically
#               implementing a LIFO stack)
#   Applications: This datastructure is used in many important problems lie
#               sliding window maximum, etc
#
from collections import deque
class kSizeStack:
    def __init__(self, k, x=[]):
        if k<1:
            raise(Exception("Size >= 1 minimum %d" % k))
        self._q = deque(x)
        self._q_size = k
    
    def push(self, item):
        if len(self._q) == self._q_size:
            dropped_element = self._q.popleft()
        self._q.append(item)

    def pop(self):
        if len(self._q)< 1:
            raise(Exception("Poping Empty Stack. Not Allowed"))
        return self._q.pop()
    

kss = kSizeStack(3)
kss.push(10)
print kss._q
kss.push(1)
print kss._q
kss.push(9)
print kss._q
kss.push(19)
print kss._q, kss._q[-1]
print kss.pop()
print kss._q, kss._q[-1]
print kss.pop()
print kss._q, kss._q[-1]
print kss.pop()
print kss._q

