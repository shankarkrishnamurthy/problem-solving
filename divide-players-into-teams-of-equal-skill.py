class Solution:
    def dividePlayers(self, skill):
        sh, ts, n, res = defaultdict(int), 0, len(skill)//2, 0
        for s in skill:
            sh[s] += 1
            ts += s
        if ts % n != 0: return -1
        se = ts//n
        for s in skill:
            if sh[s] ==0 and sh[se-s]==0: continue
            if sh[s] > 0 and sh[se - s] > 0:
                res += s*(se-s)
                sh[s] -= 1
                sh[se-s] -= 1
            else: return -1
        return res
        
