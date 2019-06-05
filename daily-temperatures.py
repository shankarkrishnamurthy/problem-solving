class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res,st = [0]*len(T), []
        for i in xrange(len(T)):
            #print i, T[i], st,res
            while st:
                if T[i] > T[st[-1]]:
                    j = st.pop()
                    res[j] = i-j
                else: break
            st.append(i)
        
        while st:
            i = st.pop()
            res[i] = 0
        return res

        

print Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print Solution().dailyTemperatures([73, 74])
print Solution().dailyTemperatures([30])
