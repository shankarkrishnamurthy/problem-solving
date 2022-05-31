class Solution:
    def totalSteps(self, nums):
        st, res = [(0,0)], 0
        for i in range(1, len(nums)):
            if nums[i] < nums[st[-1][0]]: st.append((i,1))
            else:
                cur=0
                while st and nums[i] >= nums[st[-1][0]]:
                    (ni, val) = st.pop()
                    cur = max(cur, val)
                if st: st.append((i,cur+1))
                else: st.append((i,0))
            res = max(res, st[-1][1])
            #print('i,v', (i,nums[i]),  'st', st)
        return res
