class Solution:
    def minGroups(self, intv):
        dp, res, cur=[], 0, 0
        for (s,e) in intv:
            dp.append((s,0)), dp.append((e,1))
        dp.sort()
        #print('dp',dp)
        for (v,t) in dp:
            if t == 0: cur += 1
            else: cur -= 1
            res = max(cur, res)
        return res
