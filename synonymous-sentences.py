from typing import *
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        a=[]
        for i in synonyms:
            done = False
            for j in a:
                if i[0] in j or i[1] in j:
                    j.add(i[0])
                    j.add(i[1])
                    done = True
            if done: continue
            a.append(set(i))
        #print(a)
        def ispre(i):
            for j,k in enumerate(a):
                if i in k: return j
            return -1
        s = text.split()
        dp = [s]
        for i,v in enumerate(s):
            k = ispre(v)
            if k < 0: continue
            c = []
            for e in dp:
                for t in a[k]:
                    if e[i] == t: continue
                    c.append(e[:])
                    c[-1][i] = t
            dp += c
        #print(dp, len(dp))
        res = []
        for i in dp:
            res.append(' '.join(i))
        return sorted(res) 

print(Solution().generateSentences(synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am happy today but was sad yesterday"))
print(Solution().generateSentences(synonyms = [], text = "I am happy today but was sad yesterday"))
print(Solution().generateSentences(synonyms = [['I','Me']], text = "I am happy today but was sad yesterday"))
print(Solution().generateSentences(synonyms = [['I','Me']], text = "I am happy today but I was sad yesterday"))
