class Solution:
    def minimumFinishTime(self, tires, ct, nl):
        @lru_cache(None)
        def dfs(laps):
            ml, res = len(mit), float("inf")
            for i in range(1,ml):
                if laps-i <=0: res = min(res, mit[i])
                else: res = min(res, mit[i] + ct + dfs(laps-i))
            return res
        
        mit=[0]
        for f,r in tires:
            s, t, i = 0, f, 1
            while True:
                s += t
                if i >= len(mit): mit.append(float("inf"))
                mit[i] = min(mit[i], s)
                t, i = t*r, i+1
                if ct + f < t: break
        #print(mit, 'len ', len(mit))
        res=dfs(nl)
        return res
