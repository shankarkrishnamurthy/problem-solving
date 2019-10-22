from threading import *
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.m = 1
        self.fb = Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.m > self.n:
                self.fb.release()
                return
            if not (self.m%3) and (self.m%5):
                printFizz()
                self.m += 1
            self.fb.release()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.m > self.n:
                self.fb.release()
                return
            if (self.m%3) and not (self.m%5):
                printBuzz()
                self.m += 1
            self.fb.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.m > self.n:
                self.fb.release()
                return
            if not (self.m%3) and not (self.m%5):
                printFizzBuzz()
                self.m += 1
            self.fb.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.fb.acquire()
            if self.m > self.n:
                self.fb.release()
                return
            if (self.m%3) and (self.m%5):
                printNumber(self.m)
                self.m += 1
            self.fb.release()

def printNumber(N):
    print(N,',')
def printFizz():
    print('Fizz,')
def printBuzz():
    print('Buzz,')
def printFizzBuzz():
    print('FizzBuzz,')

if __name__ == '__main__':
    a = FizzBuzz(30)
    t1 = Thread(target=a.fizz,args=(printFizz,))
    t2 = Thread(target=a.buzz,args=(printBuzz,))
    t3 = Thread(target=a.number,args=(printNumber,))
    t4 = Thread(target=a.fizzbuzz,args=(printFizzBuzz,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    print('end')
