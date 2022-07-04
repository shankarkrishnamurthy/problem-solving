class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hh, n, mv, mh, m = defaultdict(set), len(hats), 2**len(hats)-1, 0, 10**9+7
        for i in range(n):
            for h in hats[i]: 
                hh[h].add(i)
                mh = max(mh, h)
        #print('mv', mv, 'mh', mh, hh)
        @lru_cache(None)
        def dp(h, mask):
            if mask == mv: return 1
            if h > mh: return 0
            cnt = dp(h+1, mask) % m # skip this hat
            for i in range(n):
                if i in hh[h] and (1<<i)&mask == 0:
                    cnt = (cnt + dp(h+1, (1<<i)|mask)) % m
            return cnt
        return dp(1,0)
