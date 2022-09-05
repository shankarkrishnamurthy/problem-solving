class Solution:
    def maximumRobots(self, ct, rt, budget):
        def findnextmax(mq, pl, l):
            if ct[l] != -mq[0]: pl[ct[l]]+=1
            else:
                heappop(mq)
                while mq:
                    if pl[-mq[0]] == 0: break
                    pl[-mq[0]] -= 1
                    heappop(mq)
            return
        res, l, crt, mq, pl = 0,0, [0]*len(rt), [], defaultdict(int)
        for i, (a,b) in enumerate(zip(ct, rt)):
            heappush(mq, -a)
            crt[i], k = b+crt[i-1], i-l+1
            tc = -mq[0] + k*(crt[i] - (crt[l-1] if l > 0 else 0))
            while tc > budget and k > 0:
                findnextmax(mq, pl, l)
                l, k = l+1, k-1
                if k > 0: tc = -mq[0] + k*(crt[i] - (crt[l-1] if l > 0 else 0))
            res = max(res, k)
        return res
