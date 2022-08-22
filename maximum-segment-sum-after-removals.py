class Solution:
    def maximumSegmentSum(self, nums, rq):
        def sor(i,j):
            if i <= j: return ((nl[j] - nl[i-1]) if i > 0 else nl[j])
            return 0
        def getlist(a,b):
            nonlocal pend
            x,y = bisect_left(pend, a), bisect_right(pend, b)
            pend, rc = pend[:x] + pend[y:], pend[x:y]
            return rc
        def add(x, a, b): 
            if x > 0: heappush(hq, (-x, a, b))
        n, nl = len(nums), [0]*len(nums)
        for i in range(n): nl[i] = nl[i-1] + nums[i]
        cma, cl, cr = sor(0,n-1), 0, n-1
        res, pend, hq = [], [], [(-cma, cl, cr)]
        for r in rq:
            pend.append(r)
            if cl<=r<=cr:
                pend.sort()
                t, cilist = cl, getlist(cl, cr)
                while cilist:
                    heappop(hq)
                    for k in cilist:
                        add(sor(t, k-1), t, k-1)
                        t = k+1
                    add(sor(t, cr), t, cr)
                    if hq: cma, cl, cr = hq[0]
                    else: cma = 0
                    cma, t, cilist = -cma, cl, getlist(cl, cr)
            res.append(cma)
        return res
