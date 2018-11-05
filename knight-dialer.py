class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        knmap = { 0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4] }
        cur = {}
        for i in range(10): cur[i] = 1
        for i in range(1,N):
            prev = dict()
            for k in cur:
                dst = knmap[k]
                for e in dst: 
                    prev[e] = prev.get(e,0) + cur[k]
            cur = prev
            #print('cur ', cur)
        res = sum(cur.values())
        return res % (10**9 + 7)

#print(Solution().knightDialer(1))
print(Solution().knightDialer(3))
print(Solution().knightDialer(5))
print(Solution().knightDialer(9))
print(Solution().knightDialer(17))
#print(Solution().knightDialer(5000))
