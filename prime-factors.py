from library_for_lc import *
import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i != 0: continue
        else: return  False
    return True

@timeit
def primesTill(n):
    res = []
    for i in range(2,n+1):
        if isPrime(i): res.append(i)
    return res

def pFactSet(n):
    res = set()
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            res.add(i)
            while n % i == 0: n //= i
            if n == 1: break
    if n != 1: res.add(n)
    return res

#print('len', len(primesTill(10000)))

res = []
@timeit
def test():
    for i in range(2,100000):
        res.append(pFactSet(i))
test()

