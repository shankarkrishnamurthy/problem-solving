class Solution:
    def canSeePersonsCount(self, hl):
        st, res = [], [0]*len(hl)
        for i, v in enumerate(hl):
            while st and hl[st[-1]] < v:
                res[st.pop()] += 1
            if st: 
                res[st[-1]] += 1
            st.append(i)
            #print((i,v),'res',res, 'st',st)
        return res
