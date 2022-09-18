class Solution:
    def sumPrefixScores(self, words):
        wh, res, wdp = defaultdict(int), [], defaultdict(int)
        for w in words:
            for i in range(len(w)):
                wh[w[:i+1]] += 1
        for w in words:
            c = 0
            for i in range(len(w)-1,-1,-1):
                if w[:i+1] in wdp:
                    c += wdp[w[:i+1]]
                    break
                else: 
                    c += wh[w[:i+1]] 
            res.append(c)
            wdp[w] = c
        #print(dict(wh))
        return res
