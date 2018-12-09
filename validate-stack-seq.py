class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        def push_till(st,a,b):
            st += pushed[a:b]
        st,p = [], -1
        ri = {v:i for i,v in enumerate(pushed)}
        for v in popped:
            idx = ri[v]
            if idx > p:
                push_till(st, p+1, idx)
                p=idx
            elif st and v==st[-1]:
                st.pop()
            else:
                return False
            #print v, st
            
        return True

print Solution().validateStackSequences([1,2,3,4,5],[4,5,3,2,1])
print Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])
print Solution().validateStackSequences([0,1], [0,1])
print Solution().validateStackSequences([0,1,2,3,4,5,6,7,8,9,10], [3,5,7,9,10,8,6,4,2,1,0])
