class Solution:
    def mostBooked(self, n, meet):
        res, mq, endq = defaultdict(int), list(range(n)), []
        heapify(mq), meet.sort()
        for s,e in meet:
            while endq:
                if endq[0][0] > s: break
                _,r = heappop(endq)
                heappush(mq, r)
            if mq:
                r = heappop(mq)
                res[r] += 1
                heappush(endq, (e, r))
                #print((s,e),'endq', endq, 'mq', mq)
                continue
            # no free room
            ne, nr = heappop(endq)
            res[nr] += 1
            heappush(endq, (ne + e-s, nr))
            #print((s,e),'endq', endq, 'mq', mq)
        #print('res', dict(res))
        mv = max(res.values())
        for r in res:
            if res[r] == mv: return r
                
