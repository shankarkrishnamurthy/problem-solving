class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        (mi, ma) = (cost1,cost2) if cost1 < cost2 else (cost2,cost1)
        for i in range(0, total+1, ma):
            res += (total-i)//mi + 1
        return res
