class Solution:
    def totalCost(self, costs, k, c):
        l, r, hq, i, res = -1, len(costs), [], 0, 0
        for j in range(c):
            l, r = l+1, r-1
            if l == r:
                heappush(hq, (costs[l], l))
                l+=1
                break
            if l > r: break
            heappush(hq, (costs[l], l))
            heappush(hq, (costs[r], r))
        #print(l,r, hq, len(costs))
        while i < k:
            v, idx = heappop(hq)
            res, i = res+v, i+1
            #print('i',i, 'idx', idx, 'v', v, 'hq', hq, 'res', res, 'l', l, 'r', r)
            if abs(r-l) <= 1: continue
            if idx <= l:
                l += 1
                heappush(hq, (costs[l], l))
            else:
                r -= 1
                heappush(hq, (costs[r], r))
        return res
