class Solution:
    def maxConsecutive(self, bot, top, sp):
        sp.sort()
        sp.append(top+1)
        res, prev = 0, bot -1
        for v in sp:
            #print('v', v, 'floor ', v-prev-1)
            res, prev = max(res, v - prev - 1), v
        return res
