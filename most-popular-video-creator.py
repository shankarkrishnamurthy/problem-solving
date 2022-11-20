class Solution:
    def mostPopularCreator(self, creators, ids, views):
        pc, vc = defaultdict(int), {}
        for i in range(len(ids)):
            c = creators[i]
            pc[c] += views[i]
            if c not in vc: vc[c] = []
            heappush(vc[c], (-views[i], ids[i]))
        mv, res = max(pc.values()), []
        #print('mv', mv, dict(pc), vc)
        for k in sorted(pc, key=lambda x: pc[x], reverse=True):
            if pc[k] != mv: break
            #print(k, vc[k])
            res.append([k, vc[k][0][1]])
        return res
