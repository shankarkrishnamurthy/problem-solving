class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        c = 0
        for i,v in enumerate(typed):
            if name[c] == v: 
                c += 1
                continue  
            if i > 0 and v == typed[i-1]: continue
            return False
        return True
        
print Solution().isLongPressedName(name = "alex", typed = "aaleex")
print Solution().isLongPressedName(name = "saeed", typed = "ssaaedd")
print Solution().isLongPressedName(name = "leelee", typed = "lleeelee")
print Solution().isLongPressedName(name = "laiden", typed = "laiden")
