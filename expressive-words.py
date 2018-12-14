class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def count(w):
            if len(w) == 0: return []
            l,c = [w[0]],[1]
            for i in range(1,len(w)):
                if w[i] == l[-1]: c[-1] += 1
                else:
                    l.append(w[i])
                    c.append(1)
            return zip(l,c)
                
        def stretchy(w):
            #print "word ", w
            wc = count(w)
            if len(sc) != len(wc): return False
            for a,b in zip(sc,wc):
                if a[0] != b[0]: return False
                s1,w1 = a[1], b[1]
                #print a,b, s1,w1
                if s1 < 3 and s1 != w1: return False
                if s1 >= 3 and w1 > s1: return False
            return True

        sc,c = count(S),0
        #print sc
        for w in words: 
            if len(S) > 0 and len(w) > 0:
                c += stretchy(w)
            else:
                if len(S) ==0 and len(w) ==0: c += 1

        return c
                
print Solution().expressiveWords("heeellooo",["hello", "hi", "helo"])
print Solution().expressiveWords("",["hello", "hi", "helo"])
print Solution().expressiveWords("",["", "hi", "helo"])
