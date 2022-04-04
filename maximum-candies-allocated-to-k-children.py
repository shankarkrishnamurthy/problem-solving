class Solution:
    def maximumCandies(self, cl, k):
        def binsearch(v):
            nk = 0
            for i in range(len(cl)-1,-1,-1):
                nk += cl[i]//v
                if nk >= k: return True
                if cl[i] < v: return False # optimization
            return False
        
        cl.sort()
        mi, ma = 1, sum(cl)//k+1
        while mi < ma:
            mid = (mi + ma) // 2
            if binsearch(mid):
                mi = mid + 1
            else:
                ma = mid
        return mi-1
