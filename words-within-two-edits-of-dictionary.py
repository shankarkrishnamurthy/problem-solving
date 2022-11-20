class Solution:
    def twoEditWords(self, queries, dictionary):
        res, k = [], len(queries[0])
        for q in queries:
            f = False
            for d in dictionary:
                fnd, mis = True, 0
                for i in range(k):
                    if q[i] != d[i]:
                        mis += 1
                        if mis > 2:
                            fnd = False
                            break
                if fnd: 
                    f=True
                    break
            if f: res.append(q)
        return res
