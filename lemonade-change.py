class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        ch = {5:0, 10:0, 20:0}
        for v in bills:
            r = v - 5
            if r:
                if r == 15:
                    if ch[10] > 0 and ch[5] > 0:
                        ch[10] -= 1
                        ch[5] -=1
                    elif ch[5] > 2: ch[5] -= 3
                    else: return False
                else:
                    if ch[r] > 0: ch[r] -= 1
                    else: return False
            ch[v] += 1
        return True
        
print Solution().lemonadeChange([5,5,5,10,20])
print Solution().lemonadeChange([5,5,10])
print Solution().lemonadeChange([10,10])
print Solution().lemonadeChange([5,5,10,10,20])
