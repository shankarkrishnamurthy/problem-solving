class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) < 4: return stones[-1]
        o, e, res = 0, 1, stones[1]-stones[0]
        while o < len(stones):
            o, e = o + 2, e + 2
            #print(o,e, len(stones))
            if e < len(stones): res = max(res, stones[e] - stones[e-2])
            if o < len(stones): res = max(res, stones[o] - stones[o-2])
        res = max(res, stones[-1]-stones[-2])
        return res
