class Solution(object):
    def smallestSufficientTeam(self, r_s, people):
        """
        :type r_s: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        if len(r_s) == 1: return [people[0]]
        sh = {v:k for k,v in enumerate(r_s)} # hash: skill->index
        ps = [] # bitmap: skill-> people
        rs = (1 << len(r_s)) -1 # bitmap: required skill
        for i,p in enumerate(people):
            t=0
            for s in p: t |= (1 << sh[s])
            ps.append(t)
        dp = {0:[]}
        for p,s in enumerate(ps):
            for k,v in dp.items():
                whim = k | s
                if whim == k: continue
                if  whim not in dp or len(dp[whim]) > len(v) + 1:
                    dp[whim] = v + [p]
        return dp[rs]
            
print Solution().smallestSufficientTeam(r_s = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]])
print Solution().smallestSufficientTeam(r_s = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])
        
