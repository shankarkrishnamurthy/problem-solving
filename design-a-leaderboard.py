from library_for_lc import *
from typing import *
from bisect import *
from collections import deque
class Leaderboard:

    def __init__(self):
        self.h = {}
        self.q = []

    def addScore(self, pId: int, score: int) -> None:
        if pId in self.h:
            i = bisect_left(self.q,(self.h[pId],pId))
            del self.q[i]
        self.h[pId] = self.h.get(pId, 0) + score
        insort(self.q,(self.h[pId],pId))

    def top(self, K: int) -> int:
        return sum(x[0] for x in self.q[-K:])

    def reset(self, pId: int) -> None:
        i = bisect_left(self.q,(self.h[pId],pId))
        del self.q[i]
        del self.h[pId]
        
call(inp = ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"],arg = [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]])
call(inp = ["Leaderboard","addScore","top","reset","top"],arg = [[],[1,73],[1],[1],[3]])
