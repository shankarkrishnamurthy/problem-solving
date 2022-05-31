class Solution:
    def largestWordCount(self, msg, sndr):
        smh = {}
        for (m,s) in zip(msg, sndr):
            smh[s] = smh.get(s, 0) + len(m.split())
        ps = sorted((smh[k], k) for k in smh)
        #print(ps)
        return ps[-1][1]
