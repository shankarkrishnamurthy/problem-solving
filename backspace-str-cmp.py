class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sl = 0
        for i,v in enumerate(S):
            if v == '#': 
                if sl > 0: sl -= 1
            else:
                S = S[:sl] + v + S[sl+1:]
                sl += 1

        tl = 0
        for i,v in enumerate(T):
            if v == '#': 
                if tl > 0: tl -= 1
            else:
                T= T[:tl] + v + T[tl+1:]
                tl += 1
        print S[:sl], T[:tl]
        if not S[:sl] and not T[:tl]: return True
        if S[:sl] and T[:tl] and S[:sl] == T[:tl]: 
            return True
        else:
            return False

print Solution().backspaceCompare("ab#c#d", "b#ab3d")
print Solution().backspaceCompare("#", "d#")
print Solution().backspaceCompare("ab##", "c#d#")
print Solution().backspaceCompare("ab#c", "ad#c")
print Solution().backspaceCompare("a##c", "#a#c")
print Solution().backspaceCompare("a#c", "b")
