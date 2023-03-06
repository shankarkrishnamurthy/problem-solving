from bisect import *
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def nitems(A, B, x):
            res, j = len(B) - 1
            for a in A:
                while j >= 0 and a * B[j] > x: j -= 1
                res += j + 1
            return res
        nn1, nn2, m, n = bisect_left(nums1, 0), bisect_left(nums2, 0), len(nums1), len(nums2)
        h1, ma = nn1*(n-nn2)+nn2*(m-nn1), max(abs(nums1[0]), abs(nums1[-1]), abs(nums2[0]), abs(nums2[-1]))
        if k <= h1:
            l1, l2 = nums1[:nn1], [nums2[i] for i in range(n-1, nn2-1,-1)]
            l3, l4 = nums2[:nn2], [nums1[i] for i in range(m-1, nn1-1,-1)]
        else:
            k, l1, l2 = k-h1, [nums1[i] for i in range(nn1-1,-1,-1)], [nums2[i] for i in range(nn2-1,-1,-1)]
            l3, l4 = nums1[nn1:], nums2[nn2:]
        l, r = -ma*ma-1, ma*ma+1
        while l < r:
            mid = (l+r)//2
            if nitems(l1, l2, mid) + nitems(l3, l4, mid) < k: l = mid + 1
            else: r = mid
        return l

