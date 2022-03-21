class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        gtr,st, tt = sorted(enumerate(growTime), key=lambda x: x[1], reverse=True),0, 0
        for i,v in gtr:
            #print(i, 'gt ',v, 'pt ',plantTime[i], 'st ', st, 'tt ',tt)
            tt = max (tt, st + plantTime[i] + v)
            st += plantTime[i]
        return tt
