class Solution:
    def validSubarraySize(self, nums, th):
        st, l = [], []
        for i in range(len(nums)):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            li = st[-1] if st else -1
            st.append(i)
            l.append(i-li)
        st, r =[], [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            ri = st[-1] if st else len(nums)
            st.append(i)
            r[i] = ri-i
        #print('l', l, 'r', r)
        for i in range(len(nums)):
            v, k = nums[i], l[i]+r[i]-1
            if v*k > th: return k
            #print('v', v, 'k', k, 'min*k', v*k)
        return -1
