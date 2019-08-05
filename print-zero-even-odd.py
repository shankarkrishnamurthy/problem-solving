from threading import *
def printNumber(x):
    print x

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.i = 0
        self.n = n
        self.z = Event()
        self.e = Event()
        self.o = Event()
        self.z.set()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while True:
            self.z.wait()
            self.z.clear()
            self.i += 1
            if self.i > self.n: 
                self.done = True
                self.o.set()
                self.e.set()
                break
            printNumber(0)
            if self.i % 2 : self.o.set()
            else: self.e.set()
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while True:
            self.e.wait()
            self.e.clear()
            if self.i > self.n: break
            printNumber(self.i)
            self.z.set()
        
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while True:
            self.o.wait()
            self.o.clear()
            if self.i > self.n: break
            printNumber(self.i)
            self.z.set()
        
a = ZeroEvenOdd(5)
b = Thread(target=a.zero,args=([printNumber]))
c = Thread(target=a.even,args=([printNumber]))
d = Thread(target=a.odd,args=([printNumber]))

b.start()
c.start()
d.start()
