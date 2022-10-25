class Solution:
    def minimumMoney(self, trans):
        cb, v2, v1 = [], 0, 0
        for co,ca in trans:
            if co > ca: cb.append([co,ca])
            else: v2 = max(v2, co)
        if not cb: return v2
        cb.sort(key=lambda x: x[1])
        v1 = cb[-1][0]
        for i in range(len(cb)-2,-1,-1):
            v1 = v1 - cb[i][1] + cb[i][0]
        res = v2 - cb[-1][1]
        #print('v2', v2, 'v1', v1, 'len', cb)
        return v1 + max(0,res)
