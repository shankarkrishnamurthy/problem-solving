class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a%b)
        print deck
        hash = {}
        for i in deck: hash[i] = hash.setdefault(i,0) + 1
        cnt = min(hash.values())
        if cnt < 2: return False
        for k in hash:
            if hash[k] % cnt != 0:
                cnt = gcd(hash[k],cnt)
                if cnt == 1: return False

        return True

print Solution().hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2])
print Solution().hasGroupsSizeX( [1,1,2,2,2,2])
print Solution().hasGroupsSizeX( [1,1])
print Solution().hasGroupsSizeX( [1])
print Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3])
print Solution().hasGroupsSizeX( [1,2,3,4,4,3,2,1])
