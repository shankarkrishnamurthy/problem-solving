class Solution(object):
    def smallestSufficientTeam(self, r_s, people):
        """
        :type r_s: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        if len(r_s) == 1: return [people[0]]
        ph = {}
        sh = {v:k for k,v in enumerate(r_s)} # hash: skill->index
        ps = [] # bitmap: skill-> people
        rs = (1 << len(r_s)) -1 # bitmap: required skill
        for i,p in enumerate(people):
            t=0
            for s in p: 
                t |= (1 << sh[s])
                ph.setdefault(s,[]).append(i)
            ps.append(t)
        q = [(ps[p],set([p])) for p in ph[r_s[0]]]
        while True:
            tmp=[]
            for sk, pl in q:
                rem,ndx = rs & (~sk),0
                if rem == 0: return list(pl)
                while not (rem & (1<<ndx)): ndx += 1
                for p in ph[r_s[ndx]]:
                    if (sk|ps[p]) == sk: continue
                    tmp.append((sk|ps[p], pl|set([p])))
            q = tmp

            
print Solution().smallestSufficientTeam(r_s = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]])
print Solution().smallestSufficientTeam(r_s = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])

