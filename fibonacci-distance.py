class FibonacciDiv2(object):
    def find(self,N):
        if N < 4: return 0
        v1 = v2 = 1
        while True:
            tmp = v2
            v2 = v1 + v2
            v1 = tmp
            if v2 == N: return 0
            if v1 < N and v2 > N:
                return v2-N if v2-N < N-v1 else N-v1
        return 0
            
print FibonacciDiv2().find(1000000)
        
