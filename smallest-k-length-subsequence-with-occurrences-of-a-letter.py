class Solution:
    def smallestSubsequence(self, s, k, l, r):
        st, n, cl = [], len(s), 0
        nl = len([1 for c in s if c == l])
        #print('s=', s)
        #print('n=',n,'l=', l, (k,rep), 'nl=', nl)
        for i,v in enumerate(s):
            if v == l: nl -= 1
            #print( 'i=',(i,v), 'nl=', nl, 'v=', v, 'rem_let=', rep-cl, 'k-len_st', k- len(st), 'st ', st )
            while (st and                                             #  non empty st
                ((st[-1] < v and v == l and k - len(st) < r - cl) or  #  remove smaller chars in 'st' if enough 'letter' not present
                ((st[-1] > v and st[-1] != l) or                      #  remove bigger chars in 'st' as long as its not 'letter'
                (st[-1] == l and v < l and nl > r - cl))) and         #  remove 'letter' in 'st' as long as enough left to fill 'rep'
                (n-i-1 >= k - len(st))                                #  enough char to fill 'k'
                ):             
                if st.pop() == l: cl -= 1
            if len(st) < k:
                st.append(v)
                if v == l: cl += 1
        return ''.join(st)
    
