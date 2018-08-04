class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        kl = { 'A': 'a', 'B': 'b', 'C':'c', 'D':'d', 'F':'f' }
        ko = set(['a','b','c','d','e','f'])

        A = []
        for i in grid:
            A.append(list(i))
        m = len(A)
        n = len(A[0])
        #print A, m, n
        def walk(i,j):
            cnt, q = 0, set([(i,j,'')])
            while True:
                tmp = set()
                #print q, cnt
                for i,j,kt in q:
                    ktaken = set(kt)
                    if A[i][j] == '#': continue
                    if A[i][j] in kl and kl[A[i][j]] not in ktaken: continue
                    if A[i][j] in kv-ktaken: 
                        ktaken.add(A[i][j]) 

                    if not kv-ktaken: 
                        #print "Finally found a path",i,j,len(q)
                        return cnt

                    ktsj = ''.join(sorted(ktaken))
                    if i>0: tmp.add((i-1,j, ktsj))
                    if i<m-1: tmp.add((i+1,j,ktsj))
                    if j>0: tmp.add((i,j-1,ktsj))
                    if j<n-1: tmp.add((i,j+1,ktsj))

                if not tmp or cnt > 2*(m+n): return -1
                cnt += 1
                q = tmp
            return cnt
     
        def find_start():
            k = set()
            for i in range(m):
                for j in range(n):
                    if A[i][j] == '@': start = (i,j)
                    if A[i][j] in ko: k.add(A[i][j])
            return (start, k)
        
        (i,j),kv = find_start()
        #print i,j, kv
        if A[i][j] != '@': return -1
        return walk(i,j)
            
import time
start = time.clock()
print Solution().shortestPathAllKeys(["@...a",".###A","b.BCc"]) # 10
print "Time to run", time.clock()-start

"""
start = time.clock()
print Solution().shortestPathAllKeys(["@...",".##a",".b##"]) # 10
print "Time to run", time.clock()-start

start = time.clock()
print Solution().shortestPathAllKeys(["@.a.#","#####","b.A.B"])
print "Time to run", time.clock()-start

start = time.clock()
print Solution().shortestPathAllKeys(["@"])
print "Time to run", time.clock()-start

start = time.clock()
print Solution().shortestPathAllKeys(["@a"])
print "Time to run", time.clock()-start

start = time.clock()
print Solution().shortestPathAllKeys(["@.a.#","###.#","b.A.B"])
print "Time to run", time.clock()-start

start = time.clock()
print Solution().shortestPathAllKeys(["@..aA","..B#.","....b"])
print "Time to run", time.clock()-start
"""
