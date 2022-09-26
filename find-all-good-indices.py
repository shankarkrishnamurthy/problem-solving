class Solution:
    def goodIndices(self, nums, k):
        ls, rs, st = [], [0]*len(nums), deque()
        for i in range(len(nums)):
            while st and st[0] < i - k: st.popleft()
            ls.append(len(st))
            while st and nums[st[-1]] < nums[i]: st.pop()
            st.append(i)
        st, res=deque(), []
        for i in range(len(nums)-1,-1,-1):
            while st and st[0] > i+k: st.popleft()
            rs[i] = len(st)
            while st and nums[st[-1]] < nums[i]: st.pop()
            st.append(i)
        for i in range(k, len(nums)-k):
            if ls[i] >= k and rs[i] >= k: res.append(i)
        return res
