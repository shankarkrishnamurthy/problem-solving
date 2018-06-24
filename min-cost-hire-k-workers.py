class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        v = sorted(zip(quality,wage))
        q,w = zip(*v)
        msf,qc,t = float("inf"), [],0
        for i in q:
            t += i
            qc.append(t)
        print q,w
        for i in range(0, len(q) - K + 1):
            bq = qc[i]
            tw = w[i]
            for j in range(1,K):
                rq = float(q[i+j]) / float(bq)
                tw += rq*w[i]
            msf = min(msf, tw)
        return msf
        

#print Solution().mincostToHireWorkers([10,20,5], [70,50,30],2)
print Solution().mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3)
