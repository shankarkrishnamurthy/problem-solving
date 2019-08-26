from bisect import *
from library_for_lc import *
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.pi = []
        self.ist = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.pi:
            i = -self.pi.pop()
            self.ist[i].append(val)
            return
        if not self.ist: self.ist.append([val])
        else:
            if len(self.ist[-1]) < self.c: self.ist[-1].append(val)
            else: self.ist.append([val])

    def pop(self):
        """
        :rtype: int
        """
        print 'pop ', self.ist
        while self.ist and len(self.ist[-1]) == 0:
            self.ist.pop()
        if not self.ist: return -1
        val = self.ist[-1].pop()
        if not self.ist[-1]: self.ist.pop()
        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        print 'pop @ ', self.ist
        if index >= len(self.ist): return -1
        if not self.ist[index]: return -1
        insort(self.pi, -index)
        return self.ist[index].pop()

#call(inp=["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"], arg=[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]])
call(inp=["DinnerPlates","push","push","push","push","push","popAtStack","popAtStack","popAtStack","pop","pop","pop","pop","pop"], arg=[[2],[1],[2],[3],[4],[5],[0],[0],[0],[],[],[],[],[]])
