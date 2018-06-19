class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.arr = {}
        self.cnt = 0
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        if self.cnt == 0:
            self.arr[0] = 1
            self.cnt += 1
            seat = 0
        else:
            self.cnt += 1
            l,md,cd,seat = -1,0,0,0
            for i in sorted(self.arr):
                if l == -1:
                    cd,md = i,i
                    seat = 0
                else:
                    cd = (i - l)/2
                    if cd > md:
                        md = cd
                        seat = l + (i - l)/2
                l = i
            print l, i, self.arr.keys()
            cd = self.N - l - 1
            if cd > md:
                seat = self.N-1
                md = cd
            self.arr[seat] = 1
        print "Input (S) ",self.arr.keys()
        return seat

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        print "Input (L) ",self.arr
        self.cnt -= 1
        del self.arr[p]
        

# Your ExamRoom object will be instantiated and called as such:
"""
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
param_2 = obj.seat()
param_3 = obj.seat()
param_4 = obj.seat()
param_5 = obj.seat()
print param_1,param_2,param_3,param_4,param_5
