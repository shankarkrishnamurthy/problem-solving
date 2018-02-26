class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num==0: return [0]
        val = [0,1]
        c = 2
        while c < num+1:
            if 2*c <= num+1:
                val += [x+1 for x in val]
                c = 2*c
            else:
                for x in range(0,num+1-c):
                    val.append(val[x]+1)
                break
        return val

print Solution().countBits(0)
print Solution().countBits(1)
print Solution().countBits(2)
print Solution().countBits(5)
print Solution().countBits(15)
print Solution().countBits(32)
