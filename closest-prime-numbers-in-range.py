class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime(i):
            for j in range(3, int(sqrt(i))+1,2):
                if i % j == 0: return False
            return True
        if left <= 2 and right >= 3: return [2,3]
        n1, n2, l = -1, -1, left+(left%2==0)
        for i in range(l, right+1,2):
            if not prime(i): continue
            if n1 == -1: n1 = i
            elif n2 == -1: n2, pr = i, i
            else:
                if i - pr < n2 - n1: n1, n2 = pr, i
                pr = i
                if n2 - n1 == 2: break
        if n1 == -1 or n2 == -1: return [-1,-1]
        return [n1,n2]
