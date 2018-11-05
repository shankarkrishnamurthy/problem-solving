class RecentCounter(object):

    def __init__(self):
        self.p = []
        self.left = 0
        self.curr = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.left <len(self.p) and (t - self.p[self.left]) > 3000:
            print(t,self.left,self.p,self.curr)
            self.left += 1
            self.curr -= 1
        self.p.append(t)
        self.curr += 1
        return self.curr

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(642)
param_2 = obj.ping(1849)
param_3 = obj.ping(4921)
param_4 = obj.ping(5936)
param_5 = obj.ping(5957)
print(param_1,param_2,param_3,param_4,param_5)

