import math
def nCr(n,r):
    if n < r: return n
    f = math.factorial
    return f(n) / f(r) / f(n-r)

class Solution(object):
    def threeSumMulti(self, A, t):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        ch = {}
        for v in A: ch[v] = ch.setdefault(v, 0) + 1
        l1,l2,ans = {},{}, 0
        for i,v in ch.items():
            s1 = t - i
            s2 = t - 2*i
            if v>2 and 3*i == t: ans += nCr(v,3)
            for s in l2:
                if s == i: 
                    #print 'B',s,i, l2[s]
                    ans += l2[s]*v
            for s in l1:
                if v > 1 and s == 2*i: 
                    #print 'A',s,i, l1[s]
                    ans += l1[s]*nCr(v,2)
                if s > i: 
                    l1v = l1.setdefault(s,0)
                    l2[s-i] = l2.setdefault(s-i,0)
                    l2[s-i] += v*l1v

            l1[s1] = l1.setdefault(s1,0) + v
            if v > 1: l2[s2] = l2.setdefault(s2,0) + nCr(v,2)
            #print 'i',i, 'l1',l1,'l2', l2,ans
            ans %= 10**9+7

        return ans
            
print Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5],8)
print Solution().threeSumMulti([1,1,2,2,2,2],5)
print Solution().threeSumMulti([2,1,3],6)
print Solution().threeSumMulti([2,2,2],6)

