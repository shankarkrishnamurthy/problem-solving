from threading import *
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fdone = Event()
        self.bdone = Event()
        self.bdone.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bdone.wait()
            self.bdone.clear()
            printFoo()
            self.fdone.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.fdone.wait()
            self.fdone.clear()
            printBar()
            self.bdone.set()

def printFoo():
    print('Foo')
def printBar():
    print('Bar')

if __name__ == '__main__':
    a = FooBar(15)
    t1 = Thread(target=a.foo,args=(printFoo,))
    t2 = Thread(target=a.bar,args=(printBar,))
    t1.start()
    t2.start()
    
