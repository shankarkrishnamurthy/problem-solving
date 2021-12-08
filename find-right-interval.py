class Solution:
    def findRightInterval(self,i):
        def bileft(l, item, keyfunc=lambda x: x[1][0]):
            lo = 0
            hi = len(l)
            while lo < hi:
                mid = (lo+hi)//2
                if keyfunc(l[mid]) < keyfunc(item): lo = mid + 1
                else: hi = mid
            return lo
        si = sorted([(i, e) for i, e in enumerate(i)], key=lambda x:x[1])
        out = []
        print(si)
        for v in i:
            x = bileft(si, (0,[v[1],0]))
            out.append(si[x][0] if x < len(i) else -1)
        return out

print(Solution().findRightInterval([[1,2]]))
print(Solution().findRightInterval([[3,4],[2,3],[1,2]]))
print(Solution().findRightInterval([[1,4],[2,3],[3,4]]))

