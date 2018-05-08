class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        #S.sort()
        res,curr = [],[]
        for i,v in enumerate(S):
            if i == 0:
                curr=[i,-1]
                continue
            if v != S[i-1]:
                curr[1] = i-1
                if curr[1] - curr[0] > 1: res.append(curr)
                curr = [i,-1]
        curr[1] = len(S)-1
        if curr[1] - curr[0] > 1: res.append(curr)
        return res
            
#print Solution().largeGroupPositions("abbxxxxzzy")
#print Solution().largeGroupPositions("abcdddeeeeaabbbcd")
print Solution().largeGroupPositions("aaa")
