from multiprocessing  import *
def printFirst():
    print "First"
def printSecond():
    print "Second"
def printThird():
    print "Third"

class Foo(object):
    def __init__(self):
        self.f = Event()        
        self.s = Event()        


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.f.wait()
        printSecond()
        self.s.set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        self.s.wait()
        printThird()

a = Foo()
#a.first(printFirst)
a.second(printSecond)
a.third(printThird)
