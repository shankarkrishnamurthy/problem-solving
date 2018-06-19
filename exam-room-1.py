class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.arr = [0]*N
        self.cnt = 0

    def seat(self):
        """
        :rtype: int
        """
        if self.cnt == 0:
            print "Input (S) ",self.arr
            self.arr[0] = 1
            self.cnt += 1
            return 0
        else:
            self.cnt += 1
            print "Input (S) ",self.arr
            l,r,md,seat = -1,0,0,0
            while True:
                while r < len(self.arr) and self.arr[r] == 0: r+= 1
                if r == len(self.arr):
                    mdist = len(self.arr) - l - 1
                    if mdist > md: 
                        seat = r-1
                        md = mdist
                    self.arr[seat] = 1
                    return seat
                if l == -1:
                    mdist = r
                else:
                    mdist = (r-l)/2
                if mdist > md: 
                    seat = l + (r-l)/2 if l != -1 else 0
                    md = mdist
                l = r
                r +=1 

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        print "Input (L) ",self.arr
        self.cnt -= 1
        self.arr[p] = 0
        

# Your ExamRoom object will be instantiated and called as such:
obj = ExamRoom(10)
param_1 = obj.seat()
param_2 = obj.seat()
param_3 = obj.seat()
param_4 = obj.seat()
obj.leave(4)
param_5 = obj.seat()
"""
obj = ExamRoom(1000000)
param_1 = obj.seat()
param_1 = obj.seat()
param_2 = obj.seat()
param_3 = obj.seat()
param_4 = obj.seat()
param_5 = obj.seat()
param_2 = obj.seat()
param_3 = obj.seat()
param_4 = obj.seat()
param_5 = obj.seat()
"""
print param_1,param_2,param_3,param_4,param_5
