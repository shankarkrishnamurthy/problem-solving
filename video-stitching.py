class Solution(object):
    def videoStitching(self, c, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        def longestEnd(l,m):
            t,ans = l,-1
            while t <= m:
                if t in h and h[t] > m: 
                    if ans == -1 or h[ans] < h[t]: ans=t
                t += 1
            return ans
        h = {}
        for i,j in c:
            if i not in h: h[i] = j
            if i in h and j > h[i]: h[i] = j
        if 0 not in h: return -1
        b,e,cnt =0, h[0],1
        while e < T:
            rc = longestEnd(b+1,e)
            if rc == -1: return -1
            b = rc
            e = h[b]
            cnt += 1
        return cnt
        
print Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10)
print Solution().videoStitching([[0,1],[1,2]], 5)
print Solution().videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9)
print Solution().videoStitching([[0,4],[2,8]], 5)
