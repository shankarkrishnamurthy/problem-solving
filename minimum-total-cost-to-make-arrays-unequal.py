class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n, ans, total, freq = len(nums1), 0, 0, Counter()
        for i, (x, y) in enumerate(zip(nums1, nums2)): 
            if x == y: 
                freq[x] , total, ans = freq[x] + 1, total + 1, ans +i 
        key = max(freq, key=freq.get, default=None)
        most = freq[key]
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if 2*most <= total: break
            if len({x, y, key}) == 3: 
                total, ans =  total + 1, ans +i 
        return ans if 2*most <= total else -1
