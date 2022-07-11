from bisect import *
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        hl, n = [], len(nums1)
        for i in range(n): hl.append(abs(nums1[i]-nums2[i]))
        hl.sort()
        tot, hlc, l, r= k1 + k2, [0]*(n+1), 0, hl[-1] 
        for i in range(n): hlc[i+1] = hlc[i] + hl[i]
        if tot >= hlc[-1]: return 0
        while l < r:
            m = (l+r)//2
            i = bisect_left(hl, m)
            if hlc[-1] - hlc[i] - m*(n-i) > tot: l = m+1
            else: r = m
        vpp = hlc[-1] - hlc[i] - (l-1)*(n-i) - tot
        res = sum([k*k for k in hl[:i]]) + (l-1)*(l-1)*(n-i-vpp) + (l)*(l)*vpp
        #print('v=', l-1, 'i=', i, '# of v', n-i-vpp, '# of v+1', vpp) # v=l-1
        return res
