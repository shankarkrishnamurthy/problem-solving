class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a%b)
        m = gcd(targetX, targetY)
        if m == m & -m: return True # pow of 2
        return False
