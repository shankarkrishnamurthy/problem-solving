from bisect import *
class Solution(object):
    def findItinerary(self, t):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        v, hc, n = {}, {}, len(t)
        for i in t:
            insort(hc.setdefault(i[0], []), i[1])
            v[i[0]] = set()
            v[i[1]] = set()
            
        #print hc,n

        res = ["JFK"]
        def dfs(r):
            if len(res) == n+1: return True
            if r not in hc: return False
            #print 'CITY:', r ,'SET:', v
            
            for ci in range(0,len(hc[r])):
                cc = hc[r][ci]
                if ci in v[r]: continue
                v[r].add(ci)
                res.append(cc)
                rc = dfs(cc)
                if rc: return rc
                cc = res.pop()
                v[r].remove(ci)
            return False
        
        dfs("JFK")
        return res

#print Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
#print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
#print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","MAA"]])
#print Solution().findItinerary( [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]])
#print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
print Solution().findItinerary([["CBR","JFK"],["TIA","EZE"],["AUA","TIA"],["JFK","EZE"],["BNE","CBR"],["JFK","CBR"],["CBR","AUA"],["EZE","HBA"],["AXA","ANU"],["BNE","EZE"],["AXA","EZE"],["AUA","ADL"],["OOL","JFK"],["BNE","AXA"],["OOL","EZE"],["EZE","ADL"],["TIA","BNE"],["EZE","TIA"],["JFK","AUA"],["AUA","EZE"],["ANU","ADL"],["TIA","BNE"],["EZE","OOL"],["ANU","BNE"],["EZE","ANU"],["ANU","AUA"],["BNE","ANU"],["CNS","JFK"],["TIA","ADL"],["ADL","AXA"],["JFK","OOL"],["AUA","ADL"],["ADL","TIA"],["ADL","ANU"],["ADL","JFK"],["BNE","EZE"],["ANU","BNE"],["JFK","BNE"],["EZE","AUA"],["EZE","AXA"],["AUA","TIA"],["ADL","CNS"],["AXA","AUA"]])

