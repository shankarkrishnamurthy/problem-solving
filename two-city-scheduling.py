class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        #print costs
        n = len(costs)
        res = []
        for i,v in enumerate(costs):
            res.append((v[0]-v[1],i))
        res.sort()
        #print res
        ans = 0
        ans += sum([costs[res[i][1]][0] for i in range(n/2)])
        ans += sum([costs[res[i][1]][1] for i in range(n/2,n)])
        return ans
            

print Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print Solution().twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])
