class Solution:
    def parseBoolExpr(self, e):
        st, TT = [], {'t': True, 'f': False}
        for i in range(len(e)-1,-1,-1):
            if e[i] not in ('!', '&', '|'):
                if e[i] in ('t', 'f'): st.append(TT[e[i]])
                else: st.append(e[i])
                continue
            ca, v = [], st.pop()
            while v != ')':
                v = st.pop()
                if v in (True, False): ca.append(v)
            if e[i] == '&': st.append(all(ca))
            elif e[i] == '|': st.append(any(ca))
            else: st.append(not ca[0])
            #print(i, st)
        return st[0]
