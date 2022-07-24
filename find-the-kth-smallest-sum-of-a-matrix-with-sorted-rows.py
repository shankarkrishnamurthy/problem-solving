class Solution:
    def kthSmallest(self, mat, k):
        m, n,  = len(mat), len(mat[0])
        q, x, vis = [(sum([mat[i][0] for i in range(m)]), [0]*m)], 0, set()
        vis.add(tuple([0]*m))
        while q:
            (tot, arr), x = heappop(q), x+1
            #print(tot, arr, q)
            if x == k: return tot
            for i, j in enumerate(arr):
                if j+1 < n:
                    c = tot - mat[i][j] + mat[i][j+1]
                    narr = arr[:i] + [j+1] + arr[i+1:]
                    t = tuple(narr)
                    if t not in vis:
                        heappush(q, (c, narr))
                        vis.add(t)
        
