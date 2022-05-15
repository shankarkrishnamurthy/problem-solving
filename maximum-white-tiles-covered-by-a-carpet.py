class Solution:
    def maximumWhiteTiles(self, ti, cl):
        ti.sort(key=lambda x: x[0])
        csf, st, t, res = [0], [], 0, 0
        for l,r in ti:
            t += r-l + 1
            st.append(r), csf.append(t)
        for i,(l,r) in enumerate(ti):
            sp, nc = r - cl + 1, 0
            j = bisect_left(st, sp)
            if ti[j][0]<= sp: nc = sp - ti[j][0]
            sfc = csf[i+1] - csf[j]  - nc
            res = max(res, sfc)
        return res
