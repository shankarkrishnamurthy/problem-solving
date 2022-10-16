class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(a, b):
            if b <= 4: return [0, 0, 1, 2, 4][b]
            elif b == a+2: return a+1
            else:
                res = float("inf")
                for i in range(b-3, a, -4):
                    x, y = rec(a,i-1),rec(i+1,b)
                    rc = i + max(x,y) # i + max of left side or right side
                    #print('a',a,'b',b, 'i=', i, (x,y), 'rc' , rc)
                    res =  min(res, rc) # min of these possibilities
                return res
        return rec(1, n)
