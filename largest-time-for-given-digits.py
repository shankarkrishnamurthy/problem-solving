class Solution(object):
    def largestTimeFromDigits(self, B):
        """
        :type A: List[int]
        :rtype: str
        """
        A = [str(i) for i in sorted(B)]
        print A
        a = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
        b = [[2,3],[1,3],[1,2],[0,3],[0,2],[0,1]]
    
        res = []
        for h,m in zip(a,b): 
            t1 = A[h[0]]+A[h[1]]
            m1 = A[m[0]]+A[m[1]]
            if t1 <= '23' and m1 <= '59': res.append([t1,m1])
            t1 = A[h[1]]+A[h[0]]
            m1 = A[m[0]]+A[m[1]]
            if t1 <= '23' and m1 <= '59': res.append([t1,m1])
            t1 = A[h[0]]+A[h[1]]
            m1 = A[m[1]]+A[m[0]]
            if t1 <= '23' and m1 <= '59': res.append([t1,m1])
            t1 = A[h[1]]+A[h[0]]
            m1 = A[m[1]]+A[m[0]]
            if t1 <= '23' and m1 <= '59': res.append([t1,m1])
        res.sort()
        return res[-1][0]+':'+res[-1][1] if res else ''

print Solution().largestTimeFromDigits([1,2,5,4])
print Solution().largestTimeFromDigits([1,2,3,4])
print Solution().largestTimeFromDigits([5,5,5,5])
