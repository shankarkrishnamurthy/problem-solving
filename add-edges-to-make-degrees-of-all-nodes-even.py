class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        es, nc, on = set(), defaultdict(int), []
        for a,b in edges:
            nc[a], nc[b] = nc[a]+1, nc[b]+1
            es.add((a,b)), es.add((b,a))
        for k in nc:
            if nc[k] % 2 !=0: on.append(k)
            if len(on) > 4: return False
        while on:
            fnd=False
            for a,b in combinations(on,2):
                if (a,b) not in es:
                    fnd=True
                    break
            if fnd: _,__=on.remove(a),on.remove(b)
            else: break
        if not on: return True
        for i in range(1,n+1):
            if nc[i] % 2 != 0: continue
            while on:
                fnd=False
                for a,b in combinations(on,2):
                    if (a,i) not in es and (b,i) not in es:
                        fnd=True
                        break
                if fnd: _,__=on.remove(a),on.remove(b)
                else: break
            if not on: return True
        return False
