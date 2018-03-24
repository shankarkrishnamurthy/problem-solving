from collections import deque
class kSizeStack:
    def __init__(self, k, x=[]):
        self._q = deque(x)
        self._q_size = k
    def push(self, item):
        if len(self._q) == self._q_size or (not self.isEmpty() and self._q_size+self._q[0][1] <= item[1]):
            dropped_element = self._q.popleft()
        self._q.extend([item])
    def pop(self):
        return self._q.pop()
    def last(self):
        return self._q[-1]
    def first(self):
        return self._q[0]
    def isEmpty(self):
        return True if len(self._q) == 0 else False

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        kss=kSizeStack(k)
        res=[]
        for i,n in enumerate(nums):
            while not kss.isEmpty():
                if kss.last()[0] <= n: kss.pop()
                else: break
            kss.push((n,i))
            if i<k-1: continue
            res.append(kss.first()[0])
        return res

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)
print Solution().maxSlidingWindow([1,3,7,-3,5,3,6,1],3)
print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],2)
print Solution().maxSlidingWindow([1,3,7,-3,5,3,6,1],1)
print Solution().maxSlidingWindow([1],1)
