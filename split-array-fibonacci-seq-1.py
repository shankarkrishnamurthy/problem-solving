class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def mergeFib(ll1, ll2):
            newlist = []
            for l1 in ll1:
                for l2 in ll2:
                    if l1[-1] + l1[-2] == l2[0] and l1[-1] + l2[0] == l2[1]:
                        newlist.append(l1 + l2)
            return newlist

        def checkFib(v1,v2,v3):
            if v1 > 2**31-1 or v2 > 2**31-1 or v3 > 2**31-1: return False
            if v3 != (v2 + v1): return False
            return True

        def two_Part(st, en):
            for i in range(st+1,en):
                if i-st > 10: break # optimization
                for j in range(i+1,en+1):
                    if j-i > 10 or en-j+1 > 10: continue # optimization
                    v1 = int(''.join(V[st:i]))
                    v2 = int(''.join(V[i:j]))
                    v3 = int(''.join(V[j:en+1]))
                    if checkFib(v1,v2,v3): 
                        cur.append([v1,v2,v3])
                        ind.append([st,i,j])
            return
            
        V = list(S)
        st,hend = 0, {}
        q = set([0])
        while True:
            for st in q:
                newst = set()
                print st
                for end in range(3,len(V)+1):
                    cur,ind = [],[]
                    two_Part(st, end-1)
                    hend[end] = cur
                    if cur and end < len(V): 
                        newst.add(end)
                        for id in ind:
                            newst.add(id[1])
                            newst.add(id[2])
                    if st != 0 and cur: 
                        print st, end,hend
                        hend[end] = mergeFib(hend[st], hend[end])
                if hend[len(V)]: return hend[len(V)]
            if not newst: break
            q = newst
        print hend

        return []

print Solution().splitIntoFibonacci("11235813")
"""
print Solution().splitIntoFibonacci("123456579")
print Solution().splitIntoFibonacci("107374182410737418232147483647")
print Solution().splitIntoFibonacci("101")
print Solution().splitIntoFibonacci("1011")
print Solution().splitIntoFibonacci("12315")
print Solution().splitIntoFibonacci("112358130")
print Solution().splitIntoFibonacci("0123")
print Solution().splitIntoFibonacci("1101111")
print Solution().splitIntoFibonacci("68142236")
print Solution().splitIntoFibonacci("214748364721474836422147483641")
"""
