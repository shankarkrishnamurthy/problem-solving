class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st, n = [], len(nums)
        for i,v in enumerate(nums):
            while st and st[-1] > v and n-i-1 >= k-len(st): st.pop()
            if len(st) < k: st.append(v)
        return st
